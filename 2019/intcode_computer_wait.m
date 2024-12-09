function [intcode,output,outval,instruction_index,finished] = intcode_computer_wait(intcode0,inval,start_index)

%m_arg=1;
intcode=intcode0;
output="";
outval=[];
finished=false;
parsed_data=false;
instruction_index=[];
if nargin<3
 i=1;
elseif nargin==3
 i=start_index;
else
 output=strcat(output,"\n",sprintf("Number of inputs not expected.\n"));
 break
end
 
while !finished
   %intcode(i)
   command=num2str(intcode(i));
   while length(command)<5
    command=strcat("0",command);
   end
   opcode=str2num(command(4:5));
   mode_a=str2num(command(3));
   mode_b=str2num(command(2));
   mode_c=str2num(command(1));
   if or(and(mode_a!=0,mode_a!=1),and(mode_b!=0,mode_b!=1),and(mode_c!=0,mode_c!=1))
    output=strcat(output,"\n",sprintf("Problem parsing mode slection.\n"));
    break
   end
   %i
   %command 
   if opcode==1
    address_a=mode_a*(i+1-1)+(1-mode_a)*intcode(i+1);
    address_b=mode_b*(i+2-1)+(1-mode_b)*intcode(i+2);
    address_c=mode_c*(i+3-1)+(1-mode_c)*intcode(i+3);
    intcode(address_c+1)=intcode(address_a+1)+intcode(address_b+1);
    i=i+4;
   elseif opcode==2
    address_a=mode_a*(i+1-1)+(1-mode_a)*intcode(i+1);
    address_b=mode_b*(i+2-1)+(1-mode_b)*intcode(i+2);
    address_c=mode_c*(i+3-1)+(1-mode_c)*intcode(i+3);
    intcode(address_c+1)=intcode(address_a+1)*intcode(address_b+1);
    i=i+4;
   elseif opcode==99
    finished=true;
   elseif opcode==3
    fflush(stdout);
    if nargin<2
    intcode(intcode(i+1)+1)=input("Enter Value:  ");
    else
    %intcode(intcode(i+1)+1)=arguments(m_arg);
    if !parsed_data
     intcode(intcode(i+1)+1)=inval;
     parsed_data=true;
    elseif parsed_data
     output=strcat(output,"\n",sprintf("Waiting for new data.\n"));
     instruction_index=i;
     return
    end
    %m_arg++;
    end
    i=i+2;
   elseif opcode==4
    output=strcat(output,"\n",sprintf("Command 4 results in %d\n", intcode(intcode(i+1)+1)));
    outval=[outval,intcode(intcode(i+1)+1)];
    i=i+2;
    instruction_index=i;
    return 
   elseif opcode==5
    address_a=mode_a*(i+1-1)+(1-mode_a)*intcode(i+1);
    address_b=mode_b*(i+2-1)+(1-mode_b)*intcode(i+2);
    %printf("Opcode 5\n\n")
    %printf("Parameter A mode %d, address %d\n", mode_a, address_a)
    %printf("Parameter B mode %d, address %d\n", mode_b, address_b)
    %printf("Test Condition %d\n", intcode(address_a+1))
    if intcode(address_a+1)!=0
      i=intcode(address_b+1)+1;
      %printf("Jumping to index %d\n\n", i)
    else
      i=i+3;
    end
   elseif opcode==6
    address_a=mode_a*(i+1-1)+(1-mode_a)*intcode(i+1);
    address_b=mode_b*(i+2-1)+(1-mode_b)*intcode(i+2);
    if intcode(address_a+1)==0
      i=intcode(address_b+1)+1;
    else
      i=i+3;  
    end  
   elseif opcode==7
    address_a=mode_a*(i+1-1)+(1-mode_a)*intcode(i+1);
    address_b=mode_b*(i+2-1)+(1-mode_b)*intcode(i+2);
    address_c=mode_c*(i+3-1)+(1-mode_c)*intcode(i+3);
    if intcode(address_a+1)<intcode(address_b+1)
      intcode(address_c+1)=1;
    else
      intcode(address_c+1)=0; 
    end
    i=i+4;
   elseif opcode==8
    address_a=mode_a*(i+1-1)+(1-mode_a)*intcode(i+1);
    address_b=mode_b*(i+2-1)+(1-mode_b)*intcode(i+2);
    address_c=mode_c*(i+3-1)+(1-mode_c)*intcode(i+3);
    if intcode(address_a+1)==intcode(address_b+1)
      intcode(address_c+1)=1;
    else
      intcode(address_c+1)=0; 
    end   
    i=i+4;   
   else
     output=strcat(output,"\n",sprintf('Something went wrong\n'));
     break;
   end
   %intcode
end
end   