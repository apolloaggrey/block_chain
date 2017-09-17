import os


def address(ip="IPv4"):
    ip = str(ip)
    if os.name == "nt":
        os.system("ipconfig > ipconfig.txt")
        print("Microsoft Windows (nt)")
        with open("ipconfig.txt") as file:
            if "4" in ip:
                IPv4_Address = "0.0.0.0"
                for line in file:
                    if line.startswith("   IPv4"):
                        IPv4_Address = line[39:]
                        print("IPv4 Address:", IPv4_Address)
                if IPv4_Address == "0.0.0.0":
                    print("NO Connection...")
                    file.close()
                    os.system("del ipconfig.txt")
                    return("127.000.000.001")
                else:
                    file.close()
                    os.system("del ipconfig.txt")
                    return(IPv4_Address)
            elif "6" in ip:
                IPv6_Address = "0.0.0.0"
                for line in file:
                    if "IPv6" in line:
                        IPv6_Address = line[39:]
                        print("IPv6 Address:", IPv6_Address)
                if IPv6_Address == "0.0.0.0":
                    print("NO Connection...")
                    file.close()
                    os.system("del ipconfig.txt")
                    return("127.000.000.001")
                else:
                    file.close()
                    os.system("del ipconfig.txt")
                    return(IPv6_Address)
            else:
                print("localhost : 127.000.000.001")
                file.close()
                os.system("del ipconfig.txt")
                return("127.000.000.001")
        pass
    else:
        print("Unix OS")
        pass


def main():
    address("6")
    pass


if __name__ == '__main__':
    main()
