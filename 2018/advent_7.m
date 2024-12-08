clear;
tic;
data=char(importdata('day7_example.txt'));
data=char(importdata('input_7.txt'));

for i=1:length(data(:,1))
  [~,pairindex(i,:)]=regexp(data(i,:),'ep [A-Z]');
end

pair1=data(:,pairindex(:,1));
pair2=data(:,pairindex(:,2));

pairs=[pair1(:,1),pair2(:,1)];

list=unique(pairs);
choose=unique(pairs(:,2));

%first operation
seq1=sort(list(~ismember(list,choose)));
seq=seq1(1);

%remaining steps
for i=2:length(list)
  available=sort(pairs(ismember(pairs(:,1),seq),2));
  notmet=pairs(~ismember(pairs(:,1),seq),2);
  available=sort(available(~ismember(available,notmet)));
  if isempty(available)
    available=seq1(~ismember(seq1,seq));
  end
  
  seqnext=available(1);

  seq=[seq,seqnext];
  matched=ismember(pairs,seq);
  keep=~and(matched(:,1),matched(:,2));
  pairs=pairs(keep',:);
end
disp(seq)

%EUGJK

%% part 2

basetime=0;
nworkers=2;
time=0;



for i=1:length(data(:,1))
  [~,pairindex(i,:)]=regexp(data(i,:),'ep [A-Z]');
end

pair1=data(:,pairindex(:,1));
pair2=data(:,pairindex(:,2));

pairs=[pair1(:,1),pair2(:,1)];

list=unique(pairs);
choose=unique(pairs(:,2));

%first operation
seq1=sort(list(~ismember(list,choose)));
seq=seq1;

available=seq;


isworking=zeros(1,length(nworkers));
availableworkers=~isworking;

maxmoves=min(length(available),sum(availableworkers));

idx_availableworkers=find(availableworkers==1);
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ';

for i=1:maxmoves
  idx_worker=idx_availableworkers(i);
  isworking(idx_worker)=1;
  task(i)=available(i);
  [~,taskduration]=regexp(alphabet,task(i))+basetime;

end


%pseudo code
% time is zeros
% identify workers
% identify first tasks
% while not finished
% anybody available?  Yes, note who and check if work is available.  No, wait one time
% work available?  Yes, assign tasks up to the number of available help.  No, wait one time
% time +
% task finished?  Free worker.  Move task name to stack at next time
% all work finished?  End


toc