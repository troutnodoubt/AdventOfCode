function [result,matched] = stringtrim(input,pattern)
  idx=regexp(input,pattern);
  matched=false;
  if ~isempty(idx)
    matched=true;
  end
  keep=ones(1,length(input));
  keep(idx)=0;
  result=input(logical(keep));
end