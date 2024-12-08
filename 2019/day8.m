clear;clc;

%image_data_raw="123456789012";

image_data_raw=importdata("day8.txt");
image_data_raw=char(image_data_raw);

%image_data_raw="0222112222120000";

width=25;
height=6;
layer_size=width*height;

for m=1:length(image_data_raw)
 image_data(m)=str2num(image_data_raw(m));
end

n_layers=length(image_data)/layer_size;

for m=1:n_layers
 layer(m,:)=image_data(((m-1)*layer_size+1):m*layer_size);
end

for m=1:n_layers
  zero_count(m)=sum(layer(m,:)==0);
  one_count(m)=sum(layer(m,:)==1);
  two_count(m)=sum(layer(m,:)==2);
end

[~,zero_idx]=min(zero_count);
solution=one_count(zero_idx)*two_count(zero_idx);

full_image=layer(1,:);
for m=2:n_layers
  step=layer(m,:);
  full_image(full_image==2)=step(full_image==2);
end
code_image=[];
for n=1:height
  for m=1:width
    code_image(n,m)=full_image((n-1)*width+m);
  end
end
image(code_image*100)

%example  
%a(1,:)=[1,2,2,1,0,2,1]
%a(2,:)=[0,0,0,2,1,0,2]
%step=a(2,:)
%b=a(1,:)
%b(b==2)=step(b==2) 