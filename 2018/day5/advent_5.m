 clear;
 tic;
 test='dabAcCaCBAcCcaDA'
 %test=char(importdata('input_day5.txt'));
 startlength=length(test);
 match=true;
 n=0;
 while match==true
  
  idx=regexp(test,'Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz');
  firstlogical=false;
  if isempty(idx)
    firstlogical=true;
  end
  keep=ones(1,length(test));
  keep([idx,idx+1])=0;
  test=test(logical(keep))%
  idx=regexp(test,'aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ');
  secondlogical=false;
  if isempty(idx)
    secondlogical=true;
  end
  keep=ones(1,length(test));
  keep([idx,idx+1])=0;
  test=test(logical(keep))%
  match=~and(firstlogical,secondlogical);
  n=n+1;
  
end
part1=length(test);
disp(part1)

%% Part 2
test='dabAcCaCBAcCcaDA';
match=true;
clear keep;
n=0;
while match==true
  
  idx=regexp(test,'A|a');
  if isempty(idx)
    match=false;
  end
  keep=ones(1,length(test));
  keep(idx)=0;
  test=test(logical(keep))
  n=n+1;
  
end

disp "A"
disp(length(test))

toc
  