#!/usr/bin/env python
#-*-coding:utf-8-*-
import re, base64
'''
选项配置管理
__author__ = 'allen woo'
'''

def main():
    while 1:
        if add_host():
            break
        print("\n\nAgain:")

   
def add_host():
    print("================Add=====================")
    print("[Help]Input '#q' exit")
    host_ip = str_format("Host IP:", "^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    if host_ip == "#q":
        return 1
    
    host_port = str_format("Host port(Default 22):", "[0-9]+")
    if host_port == "#q":
        return 1
    
    password = str_format("Password:", ".*")
    if password == "#q":
        return 1
    password = base64.encodestring(password)
    name = str_format("User Name:", "^[^ ]+$")
    if name == "#q":
        return 1
    elif not name:
        print("[Warning]:User name cannot be emptyg")
        return 0
        
    try:
        of = open("./data/information.d")
    except:
        of = open("./data/information.d", "w")
        of.close()
        of = open("./data/information.d")
    hosts = of.readlines()
    for l in hosts:
        l = l.strip("\n")
        if not l:
            continue
        l_list = l.split(" ")
        if host_ip == l_list[1] and host_port == l_list[2]:
            print("[Warning]{}:{} existing".format(host_ip, host_port))
            return 0
    
    of.close()
    
    # save
    of = open("./data/information.d", "a")
    of.write("{} {} {} {}".format(name, host_ip, host_port, password))
    of.close()
    return 1
    
def remove_host():
    of = open("./data/information.d")
    hosts = of.readlines()
    of.close
    while 1:
        print("================Remove================")
        print("+{}+".format("-"*35))
        print("|     UserName    IP:PORT")
        l = len(hosts)
        for i in range(0, l):
            v_list = hosts[i].split(" ")
            print("+{}+".format("-"*35))
            print("| {} | {} {}:{}".format(i+1, v_list[0], v_list[1], v_list[2]))
        print("+{}+".format("-"*35))
        c = raw_input("[Remove]Choose the number or name('#q' to exit):")
        is_name = False
        is_y = False
        try:
            c = int(c)
            if c > l or c < 1:
                print("[Warning]:There is no")
                continue
            del hosts[c-1]
            is_y = True
            
        except:
            is_name = True
        if is_name:
            if c.strip() == "#q":
                break
                
            n = 0
            for l in hosts:
                if c.strip() == l.split(" ")[0].strip():
                    del hosts[c-1]
                    is_y = True 
                n += 1
                   
                    
        if not is_y:
            continue
        else:
            break
    # save
    if c.strip() == "#q":
        return
    c = raw_input("Remove?[y/n]:")
    if c.strip().upper() == "Y":
        of = open("./data/information.d", "w")
        for l in hosts:
            of.write(l)
        print("Remove the success！")


def str_format(lable, rule):
    while 1:
        print(lable)
        temp = raw_input()
        m = re.match(r"{}".format(rule), temp)
        if m:
            break
        elif "port" in lable:
            temp = 22
            break
        elif temp.strip() == "#q":
            break
        print("[Warning]:Invalid format")
    
    return temp

    
