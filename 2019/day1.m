%test

% mass=[12,14,1969,100756];

%part_1

mass=importdata('day1_1.txt');
%fuel_required=floor(mass./3)-2;
%fuel_required_sum=sum(fuel_required);

%part_2
%clear
%mass=100756;

for j=1:length(mass)

i=1;
fuel_required(i)=floor(mass(j)./3)-2;
while fuel_required(i)>0
  fuel_required(i+1)=floor(fuel_required(i)./3)-2;
  i=i+1;
end
fuel_required(fuel_required<0)=0;
fuel_required_sum(j)=sum(fuel_required);
end
fuel_required_grand_total=sum(fuel_required_sum);
