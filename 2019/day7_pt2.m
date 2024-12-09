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



for j=5:9
  for k=5:9
    for l=5:9
      for m=5:9
        for n=5:9
          

if length(unique([j,k,l,m,n]))==5
intcode_programA=intcode_program0;
intcode_programB=intcode_program0;
intcode_programC=intcode_program0;
intcode_programD=intcode_program0;
intcode_programE=intcode_program0;

%set phase settings
indexA=1;
indexB=1;
indexC=1;
indexD=1;
indexE=1;
[j,k,l,m,n]

%Phase A
[intcode_programA,~,outA,indexA,finished_A]=intcode_computer_wait(intcode_programA,j,indexA);

%Phase B
[intcode_programB,~,outB,indexB,finished_B]=intcode_computer_wait(intcode_programB,k,indexB);

%Phase C
[intcode_programC,~,outC,indexC,finished_C]=intcode_computer_wait(intcode_programC,l,indexC);

%Phase D
[intcode_programD,~,outD,indexD,finished_D]=intcode_computer_wait(intcode_programD,m,indexD);

%Phase E
[intcode_programE,~,outE,indexE,finished_E]=intcode_computer_wait(intcode_programE,n,indexE);



outE=0;
iter=1;
while !and(finished_A,finished_B,finished_C,finished_D,finished_E)
%iter
%thrust=outE

%Phase A
[intcode_programA,msgA,outA,indexA,finished_A]=intcode_computer_wait(intcode_programA,outE,indexA);

%Phase B
[intcode_programB,msgB,outB,indexB,finished_B]=intcode_computer_wait(intcode_programB,outA,indexB);

%Phase C
[intcode_programC,msgC,outC,indexC,finished_C]=intcode_computer_wait(intcode_programC,outB,indexC);

%Phase D
[intcode_programD,msgD,outD,indexD,finished_D]=intcode_computer_wait(intcode_programD,outC,indexD);

%Phase E
[intcode_programE,msgE,outE,indexE,finished_E]=intcode_computer_wait(intcode_programE,outD,indexE);

iter++;

end

results=[results;j,k,l,m,n,thrust];

end

end
end
end
end
end

max(results)

