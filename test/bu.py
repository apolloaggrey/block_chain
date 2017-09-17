import os
import sys
import time


def main():
    print("running...")
    time.sleep(1)
    run = [None,0,21,32,13,15,56,17,24,27,29,32,33,]
    script_name = str(sys.argv[0]).split("\\")[-1]
    new_script = ""
    with open(script_name, "r") as script:
        for line in script:
            if line.startswith("    run"):
                line = line.split(",")
                prefix = line[:-1]
                suffix = line[-1:]
                new_line = ""
                for x in prefix:
                    new_line += str(x) + ","
                new_line += (str(time.gmtime()[5]))
                for x in suffix:
                    new_line += "," + str(x)
                new_script += str(new_line)
            else:
                new_script += str(line)
        script.close()
    with open("bu.py", "w") as script:
        for character in new_script:
            script.write(character)
        script.close()
        pass


if __name__ == '__main__':
    main()
    try:
        os.system("start taskkill /F /IM python.exe /T" +
                  " & start python "+str(sys.argv[0]).split("\\")[-1])
        pass
    except Exception as e:
        print(e)
        pass
    finally:
        pass
