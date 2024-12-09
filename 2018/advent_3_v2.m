clear
tic;

list=['#1 @ 1,3: 4x4';
      '#2 @ 3,1: 4x4';
      '#3 @ 5,5: 2x2'];
      
list=char(textread('input_day3.txt','%s',"whitespace","","delimiter","\n"));      
      
for i=1:length(list(:,1))
  atindex=regexp(list(i,:),'@');
  colonindex=regexp(list(i,:),':');
  xindex=regexp(list(i,:),'x');
  ID(i)=str2num(list(i,2:(atindex-2)));
  coordinate(i,:)=str2num(list(i,((atindex+2):(colonindex-1))));
  size(i,1)=str2num(list(i,((colonindex+2):(xindex-1))));
  size(i,2)=str2num(list(i,((xindex+1):(end))));
  maxcanvas(i,:)=[coordinate(i,1)+size(i,1),coordinate(i,2)+size(i,2)];
end

%canvas=zeros(length(list(:,1)),max(maxcanvas(:,1))+1,max(maxcanvas(:,2))+1);
maxx=max(maxcanvas(:,1))+1;
maxy=max(maxcanvas(:,2))+1;

canvas=zeros(maxx,maxy);

%for i=1:length(list(:,1))
%  canvasID=zeros(maxx,maxy);
%  x=(coordinate(i,1)+1):(coordinate(i,1)+size(i,1));
%  y=(coordinate(i,2)+1):(coordinate(i,2)+size(i,2));
  %canvas(i,x,y)=ones(size(i,1),size(i,2));
%  canvasID(x,y)=ones(size(i,1),size(i,2))*ID(i);
%  if (canvas(x,y)~=0)
%    canvasID(x,y)=Inf
%  end
%  canvas=canvas+canvasID
%end

for i=1:length(list(:,1))
  canvasID=zeros(maxx,maxy);
  x=(coordinate(i,1)+1):(coordinate(i,1)+size(i,1));
  y=(coordinate(i,2)+1):(coordinate(i,2)+size(i,2));
  %canvas(i,x,y)=ones(size(i,1),size(i,2));
  for m=x
    for n=y
      canvasID(m,n)=ID(i);
      if (canvas(m,n)~=0)
        canvasID(m,n)=Inf;
      end
    end
  end
  canvas=canvas+canvasID;
end

%multipleclaims=sum(sum(sum(canvas)>1));  
%multipleclaims=sum(sum(canvas>1)); 
multipleclaims=sum(sum(canvas==Inf));

%% Part two
% Scan a window
solution=0;
for m=1:length(list(:,1))
if (sum(sum(canvas==ID(m)))==4)
solution=ID(m)
end
end      



toc