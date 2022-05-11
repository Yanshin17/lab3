var
    n2, i, n: integer;

begin
    readln(n);
    n2 := 0;
    for i := 1 to n do
    begin
        n2 := n2 + 2 * i - 1;
        writeln(i, ' ', n2);
    end;
end.