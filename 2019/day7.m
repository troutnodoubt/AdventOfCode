clear;clc;

%intcode_program0=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0];
%intcode_program0=[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0];
%intcode_program0=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0];

intcode_program0=importdata("day7.txt",",");



results=[];

%phase_setting=00234;
%for phase_setting=00000:44444
%phase_setting_a=int2str(phase_setting);
%while length(phase_setting_a)<5;
%  phase_setting_a=strcat("0",phase_setting_a);
%end

%for m=1:length(phase_setting_a)
%  phase_setting_vec(m)=str2num(phase_setting_a(m));
%end
for j=0:4
  for k=0:4
    for l=0:4
      for m=0:4
        for n=0:4
          

if length(unique([j,k,l,m,n]))==5
intcode_program=intcode_program0;
%Phase A
[intcode_program,~,outA]=intcode_computer(intcode_program,[j,0]);

%Phase B
[intcode_program,~,outB]=intcode_computer(intcode_program,[k,outA]);

%Phase C
[intcode_program,~,outC]=intcode_computer(intcode_program,[l,outB]);

%Phase D
[intcode_program,~,outD]=intcode_computer(intcode_program,[m,outC]);

%Phase E
[intcode_program,~,outE]=intcode_computer(intcode_program,[n,outD]);

results=[results;j,k,l,m,n,outE];

end

end
end
end
end
end

max(results)

