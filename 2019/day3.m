clear;clc;
tic

%Read in data
%data=importdata('day3_example1.txt',"\n");
%data=importdata('day3_example2.txt',"\n");
%data=importdata('day3_example3.txt',"\n");
data=importdata('day3.txt',"\n");

wire1=strsplit(char(data(1,:)),",");
wire2=strsplit(char(data(2,:)),",");


wire1dirs=cellfun(@(x) x(1),wire1);
wire2dirs=cellfun(@(x) x(1),wire2);


for m=1:length(wire1dirs);
wire1mag(m)=str2num(char(cellfun(@(x) x(2:end), wire1(m),"UniformOutput",false)));
%wire1mag(m)=cellfun(@(x) x(2:end), wire1(m),"UniformOutput",false);
end
for m=1:length(wire2dirs);
wire2mag(m)=str2num(char(cellfun(@(x) x(2:end), wire2(m),"UniformOutput",false)));
end


%Wire 1
%wire_array1=zeros(100*max(max(wire1mag),max(wire2mag)),100*max(max(wire1mag),max(wire2mag)));

%max_size=length(wire1dirs)*10;
%wire_array1=zeros(2*max_size,2*max_size);

%Put Origin at Grid Center

%origin=floor(length(wire_array1)/2);
origin=0;
idx=[origin,origin];
%idxnew=idx;
%wire_array1(idx(1),idx(2))=1;
wire1_locs=[origin,origin];

%Plot Wires

for m=1:length(wire1dirs)
  if wire1dirs(m)=="D"
    disp('WIRE1 DOWN')
    idxnew=[idx(1)+wire1mag(m),idx(2)];
    %wire_array1(idx(1):idxnew(1),idx(2))=1;
    rows=(idx(1):idxnew(1))';
    columns=idx(2)*ones(length(rows),1);
    wire1_locs=[wire1_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  elseif wire1dirs(m)=="U"
    disp('WIRE1 UP')
    idxnew=[idx(1)-wire1mag(m),idx(2)];
    %wire_array1(idxnew(1):idx(1),idx(2))=1;
    rows=flip(idxnew(1):idx(1))';
    columns=idx(2)*ones(length(rows),1);
    wire1_locs=[wire1_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  elseif wire1dirs(m)=="R"
    disp('WIRE1 RIGHT')
    idxnew=[idx(1),idx(2)+wire1mag(m)];
    %wire_array1(idx(1),idx(2):idxnew(2))=1;
    columns=(idx(2):idxnew(2))';
    rows=idx(1)*ones(length(columns),1);
    wire1_locs=[wire1_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  elseif wire1dirs(m)=="L"
    disp('WIRE1 LEFT')
    idxnew=[idx(1),idx(2)-wire1mag(m)];
    %wire_array1(idx(1),idxnew(2):idx(2))=1;
    columns=flip(idxnew(2):idx(2))';
    rows=idx(1)*ones(length(columns),1);
    wire1_locs=[wire1_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  end
end


%Wire 2
%wire_array2=zeros(length(wire_array1),length(wire_array1));


%Put Origin at Grid Center
idx=[origin,origin];
%idxnew=idx;
%wire_array1(idx(1),idx(2))=1;
wire2_locs=[origin,origin];

%Plot Wires

for m=1:length(wire2dirs)
  if wire2dirs(m)=="D"
    disp('WIRE2 DOWN')
    idxnew=[idx(1)+wire2mag(m),idx(2)];
    rows=(idx(1):idxnew(1))';
    columns=idx(2)*ones(length(rows),1);
    wire2_locs=[wire2_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  elseif wire2dirs(m)=="U"
    disp('WIRE2 UP')
    idxnew=[idx(1)-wire2mag(m),idx(2)];
    rows=flip(idxnew(1):idx(1))';
    columns=idx(2)*ones(length(rows),1);
    wire2_locs=[wire2_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  elseif wire2dirs(m)=="R"
    disp('WIRE2 RIGHT')
    idxnew=[idx(1),idx(2)+wire2mag(m)];
    columns=(idx(2):idxnew(2))';
    rows=idx(1)*ones(length(columns),1);
    wire2_locs=[wire2_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  elseif wire2dirs(m)=="L"
    disp('WIRE2 LEFT')
    idxnew=[idx(1),idx(2)-wire2mag(m)];
    columns=flip(idxnew(2):idx(2))';
    rows=idx(1)*ones(length(columns),1);
    wire2_locs=[wire2_locs;rows(2:end),columns(2:end)];
    idx=idxnew;
  end
end

disp("wires plotted")


   
%Find Intersections

%wire_array2(origin,origin)=0;
%wire_array=wire_array1+wire_array2;
%[a,b]=find(wire_array==2);
%cross=[0,0];
%count=1;
%for m=1:length(wire1_locs)
%  for n=1:length(wire2_locs)
%    sprintf("Run %d of %d", count, length(wire1_locs)*length(wire2_locs)) 
%    count++
%    if and(wire1_locs(m,1)==wire2_locs(n,1),wire1_locs(m,2)==wire2_locs(n,2))
%      cross=[cross;wire1_locs(m,:)];
%    end
%  end
%end

[matched,match_idx]=ismember(wire1_locs,wire2_locs,"rows");

%Calculate Distance
%distance=min(abs(a-origin)+abs(b-origin));
cross=wire1_locs(matched,:);
distance=abs(cross(:,1))+abs(cross(:,2));
distance=distance(distance!=0);
distance=min(distance);


% Part 2

%Will need to clean up wire_locs to remove duplicates when changing direction

[matched2,match_idx2]=ismember(wire2_locs,wire1_locs,"rows");

wire2_sorted=sortrows([wire2_locs(matched2,:),match_idx2(matched2)-1]);
wire1_sorted=sortrows([wire1_locs(matched,:),match_idx(matched)-1]);

steps=wire1_sorted(:,3)+wire2_sorted(:,3);
steps=steps(steps!=0);
minstep=min(steps);






toc