clear
tic;
%ID=['abcdef';
%    'bababc';
%    'abbcde';
%    'abcccd';
%    'aabcdd';
%    'abcdee';
%    'ababab'];

ID=char(textread('input_day2.txt','%s'));

test='abcdefghijklmnopqrstuvwxyz';


% Generate count matrix
count=zeros(length(ID),length(test));
for i=1:length(test)
 letter=test(i);
 [idx,~]=strchr(ID,letter);
 for j=1:length(ID)
  count(j,i)=sum(idx==j);
 end
end

% Count ID by ID for twos or threes 
twos=0;
threes=0;
for j=1:length(ID)
 twos=twos+(sum(count(j,:)==2)>0);
 threes=threes+(sum(count(j,:)==3)>0);
end

chksum=twos*threes;

%% part two
%ID=['abcde';
%    'fghij';
%    'klmno';
%    'pqrst';
%    'fguij';
%    'axcye';
%    'wvwyz'];

for j=1:length(ID)
 for k=j:length(ID)
  switched=sum(~(ID(j,:)==ID(k,:)));
  if switched==1
   ID(j,:)
   ID(k,:)
   solution=ID(j,(ID(j,:)==ID(k,:)));
  end
 end
end

toc