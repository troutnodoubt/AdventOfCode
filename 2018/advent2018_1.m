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
freq=zeros(1,length(sequence)+1);
for i=(1:length(sequence))
freq(i+1)=sum(sequence(1:i));
end

for m=1:length(freq)
%freq_test(m)=sum(freq==freq(m));
if (sum(freq==freq(m))>1)
repeatmatch=1;
freq(m)
end
end





%[seq_unique,index_unique]=unique(freq');
%freq_test=freq;
%freq_test(index_unique)=0;
%freq_test=freq_test(~ismember(1:length(freq_test),index_unique));
%repeatmatch=sum(freq_test);
repeat=repeat+1;
sequence=[sequence;sequence0];
%if repeat==1000
%repeatmatch=1;
%end
end
%freq_test=freq_test(freq_test~=0);
%solution=freq_test(1);
toc