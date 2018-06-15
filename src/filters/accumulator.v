module accumulator #(parameter Nbits = 14)
             (X, Y, CLK, CLR);

  input CLK;
  input CLR;

  input  [Nbits-1:0] X;
  output [Nbits-1:0] Y;
  reg [Nbits-1:0] accum=0; 

  //reg Y;

  always @(posedge CLK or posedge CLR)
  begin
     if (CLR)
      accum[Nbits-1:0] <= 0;
     else
       accum[Nbits-1:0] <= accum[Nbits-1:0] + X[Nbits-1:0];
  end

  assign Y = accum;

endmodule
