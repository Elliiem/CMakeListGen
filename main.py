import os

project = input()
dir = "/home/elliem/cpp/" + project

cppFiles = os.listdir(dir + "/src")
cppString = ""

for x in cppFiles:
    cppString += "src/"+x+" "

cppString = list(cppString)
cppString[-1] = ""
cppString = "".join(cppString)

CMakeList = open(dir + "/CMakeLists.txt", "w")
Packages = open(dir + "/packages.txt", "r")


CMakeList.write("cmake_minimum_required(VERSION 3.7)\n")
CMakeList.write(f"project({project})\n")
CMakeList.write("\n")

packageString = ""

for lines in Packages:
    line = lines.replace("\n","")
    CMakeList.write(f"find_package({line} REQUIRED)\n")
    CMakeList.write("include_directories(${"+line+"_INCLUDE_DIRS})\n")
    CMakeList.write("\n")
    packageString += line+" "

packageString = list(packageString)
packageString[-1] = ""
packageString = "".join(packageString)

CMakeList.write(f"add_executable({project} {cppString})\n")
CMakeList.write(f"target_include_directories({project} PRIVATE include/)\n")
CMakeList.write(f"target_link_libraries({project} {packageString})\n")

