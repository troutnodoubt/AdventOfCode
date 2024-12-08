tic;
clear

sequence=load('input.txt');
%sequence=[1,-1]';
%sequence=[3,3,4,-2,-4]';
%sequence=[-6, +3, +8, +5, -6]';
%sequence=[+7, +7, -2, -7, -4]';

sequence0=sequence;
final_freq=sum(sequence);
repeat=0;
repeatmatch=0;

while (repeatmatch==0)
%freq=zeros(1,length(sequence)+1);
%for i=(1:length(sequence))
%freq(i+1)=sum(sequence(1:i));
%end

freq=cumsum(sequence)';
freq=[0,freq];


[~,b]=unique(freq');
c=1:length(freq);
list=freq(~ismember(c,b));
repeatmatch=sum(~ismember(c,b));

repeat=repeat+1;
sequence=[sequence;sequence0];

%if repeat==5
%repeatmatch=1;
%end

end

[~,idx]=ismember(list,freq);
solution=freq(min(idx));

toc