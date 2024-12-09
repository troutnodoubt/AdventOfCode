clear;clc;
format long;
intcode0=importdata("day9.txt",",");
%intcode0=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99];
%intcode0=[1102,34915192,34915192,7,4,7,99,0];
%intcode0=[104,1125899906842624,99];
[intcode,output,outval]=intcode_computer(intcode0);