import sys as DVDNVSVBUSHNB
import time as YRYGFBUYEGBFU


def main():
    NIFNVNIJCBDB = str(DVDNVSVBUSHNB.argv[0]).split("\\")[-1]
    NBJYVJHHVYSY = ""
    with open(NIFNVNIJCBDB, "r") as YTFYBTFBVDYF:
        for GBGBYFFHTF in YTFYBTFBVDYF:
            if GBGBYFFHTF.startswith("    JBVFUSVNSVUB"):
                GBGBYFFHTF = GBGBYFFHTF.split(",")
                TDVUYTDFTVRDT = GBGBYFFHTF[:-1]
                DSCRDVHTRHGB = GBGBYFFHTF[-1:]
                VFJTRFTYFHJGC = ""
                for CDHRTCVTYJDY in TDVUYTDFTVRDT:
                    VFJTRFTYFHJGC += str(CDHRTCVTYJDY) + ","
                VFJTRFTYFHJGC += (str(YRYGFBUYEGBFU.gmtime()[5]))
                for CDHRTCVTYJDY in DSCRDVHTRHGB:
                    VFJTRFTYFHJGC += "," + str(CDHRTCVTYJDY)
                NBJYVJHHVYSY += str(VFJTRFTYFHJGC)
            else:
                NBJYVJHHVYSY += str(GBGBYFFHTF)
        YTFYBTFBVDYF.close()
    with open(NIFNVNIJCBDB, "w") as YTFYBTFBVDYF:
        for VFTYFUYFVVYD in NBJYVJHHVYSY:
            YTFYBTFBVDYF.write(VFTYFUYFVVYD)
        YTFYBTFBVDYF.close()
        pass

if __name__ == '__main__':
    JBVFUSVNSVUB = [None, 43, ]
    main()
