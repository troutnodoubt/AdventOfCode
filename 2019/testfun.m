

function [out_vec,m,value]=testfun(in_vec,m,nreturn)
  value=[];
  if !exist("m")
    m=0;
  end
  
  if !exist("nreturn")
    nreturn=[];
  end
  
    
  out_vec=in_vec;
  for n=1:length(in_vec)
    if n>m
      out_vec(n)=n*in_vec(n);
      m=n;
    end
    if n==nreturn
      value=out_vec(n);
      return
    end
  end
end
