"""Small MCP client for AL-Naqawa. Python standard library only."""
import argparse,json,sys,urllib.request,urllib.error
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('--endpoint',default='https://alnaqawa.com/mcp')
    sub=p.add_subparsers(dest='command',required=True);sub.add_parser('list')
    call=sub.add_parser('call');call.add_argument('tool');call.add_argument('--input',type=Path,required=True);call.add_argument('--save',type=Path)
    a=p.parse_args();version=None
    def post(method,params,request_id):
        headers={'Content-Type':'application/json','Accept':'application/json, text/event-stream','User-Agent':'AL-Naqawa-Skill/1.0'}
        if version:headers['MCP-Protocol-Version']=version
        req=urllib.request.Request(a.endpoint,data=json.dumps({'jsonrpc':'2.0','id':request_id,'method':method,'params':params}).encode(),headers=headers)
        try:
            with urllib.request.urlopen(req,timeout=30) as r:
                mime=r.headers.get('Content-Type','')
                body=r.read(1048577)
                if len(body)>1048576:raise RuntimeError('The response exceeded the supported size.')
                if 'application/json' in mime:out=json.loads(body)
                elif 'text/event-stream' in mime:
                    messages=[]
                    for event in body.decode('utf-8').replace('\r\n','\n').split('\n\n'):
                        lines=[line[5:].lstrip() for line in event.splitlines() if line.startswith('data:')]
                        if lines:messages.append(json.loads('\n'.join(lines)))
                    out=next((m for m in reversed(messages) if m.get('id')==request_id and ('result' in m or 'error' in m)),None)
                    if out is None:raise RuntimeError('No matching MCP response was returned.')
                else:raise RuntimeError('The endpoint did not return a supported MCP response.')
        except urllib.error.HTTPError as e:raise RuntimeError('MCP request returned HTTP '+str(e.code)) from None
        except urllib.error.URLError:raise RuntimeError('Could not connect to the MCP endpoint.') from None
        if 'error' in out:raise RuntimeError('MCP error: '+out['error'].get('message','Request failed'))
        return out['result']
    init=post('initialize',{'protocolVersion':'2025-11-25','capabilities':{},'clientInfo':{'name':'al-naqawa-skill','version':'1.0.0'}},1)
    version=init['protocolVersion']
    if a.command=='list':print(json.dumps(post('tools/list',{},2),ensure_ascii=False,indent=2));return
    arguments=json.loads(a.input.read_text(encoding='utf-8-sig'))
    result=post('tools/call',{'name':a.tool,'arguments':arguments},2)
    if result.get('isError'):raise RuntimeError('\n'.join(c.get('text','') for c in result.get('content',[]) if c.get('type')=='text'))
    data=result.get('structuredContent')
    if data is None:data=json.loads(next(c['text'] for c in result['content'] if c['type']=='text'))
    if a.save:
        if a.tool!='generate_timetable' or not isinstance(data.get('text'),str):raise RuntimeError('--save is only supported for generated timetable files.')
        extension='.'+data['file_name'].rsplit('.',1)[1]
        if a.save.suffix.lower()!=extension:raise RuntimeError('Output extension must match '+extension)
        with a.save.open('x',encoding='utf-8',newline='') as f:f.write(data['text'])
        print(json.dumps({'saved':str(a.save.resolve()),'mime_type':data['mime_type'],'warnings':data.get('warnings',[])},ensure_ascii=False));return
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,RuntimeError) as e:print(str(e),file=sys.stderr);raise SystemExit(1)
