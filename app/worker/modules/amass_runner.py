import subprocess

def amass_wrapper(search_key:str):
    
    print('in process ', search_key, flush=True)
    try:
        results = subprocess.run(['amass', 'enum' ,'-d', search_key], capture_output=True, text=True)
        return results.stdout

    except subprocess.CalledProcessError as exc:
        print(
            f"Process failed because did not return a successful return code. "
            f"Returned {exc.returncode}\n{exc}"
        )
    except subprocess.TimeoutExpired as exc:
        print(f"Process timed out.\n{exc}")