import time
import shlex
import argparse
import traceback
import subprocess


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="token", help="your ngrok authtoken. see https://dashboard.ngrok.com/get-started/your-authtoken")
    parser.add_argument(dest="password", help="your code-server password. example: 123456")
    parser.add_argument(dest="region", help='ngrok server region [us, eu, au, ap, sa, jp, in]')
    args = parser.parse_args()

    # Export environment variables to shell scripts
    with open("/root/env.sh", "w") as file:
        with open("/root/.env", "r") as env:
            for line in env:
                i = line.find("=")
                file.write('export {}="{}"\n'.format(line[:i], line[i+1:].strip()))

    print("authorize ngrok token...")
    subprocess.Popen(shlex.split(f"ngrok authtoken {args.token}")).wait()
    print("starting ngrok...")
    ngrok_process = subprocess.Popen(shlex.split(f"ngrok http 8080 --log stdout --region {args.region}"))
    print("starting code-server...")
    code_server_process = subprocess.Popen(shlex.split("code-server"), env={"PASSWORD": args.password})

    try:
        while True:
            time.sleep(1)
    except:
        ngrok_process.kill()
        ngrok_process.wait()
        code_server_process.kill()
        code_server_process.wait()
        traceback.print_exc()