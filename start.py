# coding: utf-8
import os
import time
import datetime
import shutil

def getList(rootDir):
    t_list = []
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            t_list.append(os.path.join(root, d).replace(rootDir, ""))
        for f in files:
            t_list.append(os.path.join(root, f).replace(rootDir, ""))
    return t_list
def createFolder(p_folder):
    if not os.path.isdir(p_folder):
        os.makedirs(p_folder)
        time.sleep(0.1)
def getTimeSuffix():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')
def copyFile(o_file, dst):
    if os.path.isfile(o_file):
        shutil.copyfile(o_file, dst)
def commentFormat(comment):
    print ""
    print sepratorStart
    print "*****  " + comment
    print sepratorEnd

list_img_suffix = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
def isInCollection(value, list_in=list_img_suffix):
    if "." + value.lower().split(".")[-1] in list_in:
        return True
    return False

def isImg(value, list_in=list_img_suffix):
    last = value.split("\\")[-1]
    if "." in last and "." + value.lower().split(".")[-1] not in list_in:
        return False
    return True


if __name__ == '__main__':
    # There are 2 values for copyAnyway 1. True 2. False
    copyAnyway = False
    folder_ExpectedResult = r'D:\Pro_2.0_screenshots_To_BYS-sorting'
    folder_ActualResult = r'D:\Pro_2.0_screenshots_To_BYS-sorting - Copy'

    sepratorStart = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    sepratorEnd = "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    extra_errors = 0
    missing_errors = 0
    list_ExpectedResult = getList(folder_ExpectedResult)
    list_ActualResult = getList(folder_ActualResult)
    commentFormat("Extra folder(s)/file(s):")
    for l in list_ActualResult:
        if isImg(l) and l not in list_ExpectedResult:
            extra_errors += 1
            print "%0004d > [%s]" % (extra_errors, folder_ActualResult + l)
    commentFormat("Missing folder(s)/file(s):")
    for l in list_ExpectedResult:
        if isImg(l) and l not in list_ActualResult:
            missing_errors += 1
            print "%0004d > [%s]" % (missing_errors, folder_ActualResult + l)
    if (extra_errors == 0 and missing_errors == 0) or copyAnyway:
        commentFormat("Coping files, please wait...")
        fn = r"D:/" + getTimeSuffix()
        createFolder(fn)
        list_newExpected = os.walk(folder_ExpectedResult).next()[1]
        for i in list_newExpected:
            createFolder(os.path.join(fn, i))
            createFolder(os.path.join(fn, i + "_actual"))
        for l in list_ExpectedResult:
            start = l.split("\\")[1]
            last = l.split("\\")[-1]
            if isInCollection(last) and start in list_newExpected:
                copyFile(folder_ExpectedResult + l, os.path.join(fn, start, last))
                copyFile(folder_ActualResult + l, os.path.join(fn, start + "_actual", last))
        commentFormat("Done! Please find the result in [%s]." % fn)
    else:
        commentFormat("Please correct the error(s) at first.")




