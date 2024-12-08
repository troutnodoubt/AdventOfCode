%input=char('1,9,10,3,2,3,11,0,99,30,40,50');
%intcode=cell2mat(textscan(input,'%d',"delimiter",","))

%intcode=[1,0,0,0,99];
%intcode=[2,3,0,3,99];
%intcode=[2,4,4,5,99,0];
%intcode=[1,1,1,4,99,5,6,0,99];
%intcode0=importdata('day_2.txt',",");
%intcode=intcode0;
%intcode(1+1)=12;
%intcode(2+1)=2;

%intcode=[3,0,4,0,99];

% [3,225][1,225,6,6][1100,1,238,225][104,0]
% 1: Prompt for 1, stored at address 225 (i=226)
% 2: Add value at address 225 (1), to the value at address 6 (1100) and write it to address 6, now 1101
% 3: Add 1+238 and store in address 225
% 4: Display the value of address 0 (3)

intcode=importdata('day_5.txt',",");
%intcode=[3,9,8,9,10,9,4,9,99,-1,8];
%intcode=[3,9,7,9,10,9,4,9,99,-1,8];
%intcode=[3,3,1108,-1,8,3,4,3,99];
%intcode=[3,3,1107,-1,8,3,4,3,99];
%intcode=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9];

finished=false;
i=1;
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
    printf("Problem parsing mode slection.\n")
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
    intcode(intcode(i+1)+1)=input("Enter Value:  ");
    i=i+2;
   elseif opcode==4
    printf("Command 4 results in %d\n", intcode(intcode(i+1)+1))
    i=i+2; 
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
     printf('Something went wrong\n')
     break;
   end
   %intcode
end
      