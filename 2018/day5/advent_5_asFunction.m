 clear;
 tic;
 test='dabAcCaCBAcCcaDA'
 %test=char(importdata('input_day5.txt'));
 startlength=length(test);
 match=true;
 n=0;
 while match==true
  
  pattern1='Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz';
  pattern2='aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ';
  combinedpattern=[pattern1,pattern2];
  [test,match]=stringtrim(test,combinedpattern);
  
end
part1=length(test);
disp(part1)
disp(test)
%% Part 2
toc


  