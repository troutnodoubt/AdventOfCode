clear;clc;tic;
%asteroid_map=importdata("day10_example1.txt");
%asteroid_map=importdata("day10_example2.txt");
asteroid_map=importdata("day10.txt");
asteroid_map=char(asteroid_map);
limits=size(asteroid_map);

asteroid_pts=[];
for m=1:limits(1)
  for n=1:limits(2)
    if asteroid_map(m,n)=="#"
      asteroid_pts=[asteroid_pts;m,n];
    end
  end
end
best=0;
solution=[];
map=zeros(size(asteroid_map));
for m=1:length(asteroid_pts)
  y_vec=asteroid_pts(:,1)-asteroid_pts(m,1);
  x_vec=asteroid_pts(:,2)-asteroid_pts(m,2);
  y_vec=-y_vec;
  mag=sqrt(x_vec.*x_vec+y_vec.*y_vec);
  unit_vectors=[x_vec,y_vec]./mag;
  unit_vectors=round(unit_vectors*10000)/10000;
  
  n_observed=length(unique(unit_vectors,"rows"))-1;
  %m
  %n_observed
  
  map(asteroid_pts(m,1),asteroid_pts(m,2))=n_observed;
  if n_observed>best
    best=n_observed;
    bestm=m;
    solution=asteroid_pts(m,:)-1;
    solution=fliplr(solution);
    theta=atan2d(y_vec,x_vec);
    theta=theta-90;
    theta=-theta;
    theta=mod(theta+360,360);
    list=[x_vec,y_vec,mag,theta];
    list=round(list*1000000)/1000000;
  end
  
end
list=list(~list(:,3)==0,:);
list=sortrows(list,4);
unique_angles=unique(list(:,4));
%count_index=1;
result=[];
for m=1:length(unique_angles)
  angle_index=ismember(list(:,4),unique_angles(m));
  subset=list(angle_index,:);
  subset=sortrows(subset,3);
  [nrows,ncols]=size(subset);
  for n=1:nrows
    subset(n,4)=subset(n,4)+(n-1)*360;
  end
  
  result=[result;subset];
    %count_index++;
  
  
end
result=sortrows(result,4);
result(:,5)=solution(1)+result(:,1);
result(:,6)=solution(2)-result(:,2);
%result=result(and(result(:,1)~=0,result(:,2)~=0));
answer=(result(200,5))*100+result(200,6);
toc