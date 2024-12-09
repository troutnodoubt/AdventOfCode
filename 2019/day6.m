
clear;clc;
tic;
%orbit_map=importdata("day6_example.txt");
%orbit_map=textread("day6_example.txt","%s");
%orbit_map=importdata("day6_short.txt",")");
orbit_map=textread("day6.txt","%s");

path=struct();

for m=1:length(orbit_map)
pair=strsplit(char(orbit_map(m)),")");
orbitted(m)=pair(1);
orbitter(m)=pair(2);
end
count=0;
%for m=1:length(orbitter)
%for m=1
%child=orbitter(m);
childlist=["YOU";"SAN"];
childlist=cellstr(childlist);
for m=1:length(childlist)
  child=childlist(m);
  count=0;
  list=child;
  list=cellstr(list);
while !strcmp(char(child),"COM")
  %sprintf("%s ->", char(child))
  %parent=orbitted(strfind(char(orbitter),char(child)))
  parent=orbitted(strmatch(char(child),char(orbitter)));
  child=parent;
  list=[list;child];
  if isempty(parent)
    break
   end
   %fflush(stdout)
  %disp(m)
  count=count+1;
  
  %disp(count)
end
  %printf("\n");
  orbit_count(m)=count;
  path=setfield(path,char(childlist(m)),list);
end

YOUpathlength=sum(!ismember(path.YOU,path.SAN));
SANpathlength=sum(!ismember(path.SAN,path.YOU));

transfers=YOUpathlength+SANpathlength-2;
  
toc
