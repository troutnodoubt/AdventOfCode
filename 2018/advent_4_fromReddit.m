G = zeros(5000,60);
x = sort(importdata('input_day4.txt'));
for i=1:size(x,1)
    idx = strfind(x{i},'#');
    if idx
        awake = true;
        ID = sscanf(x{i}(idx+1:end),'%f');
        continue
    end
    t = str2double(x{i}(16:17));
    G(ID,t+1:end) = G(ID,t+1:end)-1+2*awake;
    awake = ~awake;
end
[~,a] = max(sum(G,2));
[~,b] = max(G(a,:));
[~,c] = max(max(G,[],2));
[~,d] = max(G(c,:));
disp((b-1)*a) % Part 1
disp((d-1)*c) % Part 2