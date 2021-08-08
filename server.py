import uvicorn
import secure
import subprocess
import sys
import os
import asyncio
from threading import Thread


DEBUG = True
_host_ = '127.0.0.1'
_port_ = 1234 if DEBUG else 5001
server = secure.Server().set("Secure")
csp = (
    secure.ContentSecurityPolicy()
        .default_src("'none'")
        .base_uri("'self'")
        .connect_src("'self'" "localhost")
        .frame_src("'none'")
        .img_src("'self'", "static.spam.com")
)
hsts = secure.StrictTransportSecurity().include_subdomains().preload().max_age(2592000)
referrer = secure.ReferrerPolicy().no_referrer()
permissions_value = (secure.PermissionsPolicy().geolocation("self", "'spam.com'").vibrate())
cache_value = secure.CacheControl().must_revalidate()
secure_headers = secure.Secure(
    server=server,
    csp=csp,
    hsts=hsts,
    referrer=referrer,
    permissions=permissions_value,
    cache=cache_value,
)

if __name__ == '__main__':
    '''ON_POSIX = 'posix' in sys.builtin_module_names
    __var__ = os.path.join(os.path.dirname(__file__))
    _p_ = subprocess.Popen(
        ['py', f'{__var__}/check_tables.py'],
        shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE, universal_newlines=True,
        bufsize=1, close_fds=ON_POSIX)'''
    
    uvicorn.run(
        'main:app',
        host=_host_,
        port=_port_,
        reload=True,
        proxy_headers='Strict-Transport-Security: 2592000',
        ssl_certfile="key/certificate.crt",
        ssl_keyfile="key/private.key"
    )
