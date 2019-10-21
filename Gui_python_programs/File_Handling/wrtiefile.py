def main():
    fhandle=open("pytextfile",'w+')
    fhandle.write("this is write method in file using python")
    fhandle.seek(0)
    print(fhandle.read())



if __name__=='__main__':
    main()