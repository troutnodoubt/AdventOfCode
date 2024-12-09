%input=char('1,9,10,3,2,3,11,0,99,30,40,50');
%intcode=cell2mat(textscan(input,'%d',"delimiter",","))

%intcode=[1,0,0,0,99];
%intcode=[2,3,0,3,99];
%intcode=[2,4,4,5,99,0];
%intcode=[1,1,1,4,99,5,6,0,99];
intcode0=importdata('day_2.txt',",");
solved=false;
for noun=0:99
if solved
break
end
for verb=0:99
intcode=intcode0;
intcode(1+1)=noun;
intcode(2+1)=verb;
for i=1:4:length(intcode)
   %intcode(i)
   a=intcode(i+1);
   b=intcode(i+2);
   if intcode(i)==1
    intcode(intcode(i+3)+1)=intcode(a+1)+intcode(b+1);
   elseif intcode(i)==2
    intcode(intcode(i+3)+1)=intcode(a+1)*intcode(b+1);
   elseif intcode(i)==99
    break
   else
     sprintf('Something went wrong\n')
     break;
   end
   %intcode
end
if intcode(0+1)==19690720
  noun
  verb
  sol=100*noun+verb
  solved=true;
end
if solved
break
end

end

end
      