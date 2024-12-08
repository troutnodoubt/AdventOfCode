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

maxx=max(maxcanvas(:,1))+1;
maxy=max(maxcanvas(:,2))+1;

canvas=zeros(maxx,maxy);


for i=1:length(list(:,1))
  canvasID=zeros(maxx,maxy);
  x=(coordinate(i,1)+1):(coordinate(i,1)+size(i,1));
  y=(coordinate(i,2)+1):(coordinate(i,2)+size(i,2));
  canvasID(x,y)=1;
  canvas=canvas+canvasID;
end

multipleclaims=sum(sum(canvas>1)); 


%% Part two
solution=0;
for i=1:length(list(:,1))

  x=(coordinate(i,1)+1):(coordinate(i,1)+size(i,1));
  y=(coordinate(i,2)+1):(coordinate(i,2)+size(i,2));
  if (all(canvas(x,y)==1))
    solution=ID(i);
  end
end      


toc