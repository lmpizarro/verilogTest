`timescale 1ns/1ps
module ACC1632(X, Y, clk, clr);
  input signed [15:0] X;
  output signed [31:0] Y;
  reg signed [31:0] accum;

  input clk, clr;
 
  assign Y[31:0] = accum[31:0];
  always @(posedge clk)
  begin
    if (clr) accum <= 0;
    else accum <= $signed(accum + {{16{X[15]}},X});
  end
endmodule


module tb_zero();
 
  reg signed [15:0] x;
  reg clk; 
  wire outP, outN, out; 
  reg clr;
  integer i;

 zero_cross ZC(.X(x), .outNP(outP), .outPN(outN), .out(out), .clk(clk), .clr(clr));

  initial begin
    $dumpfile("simple.vcd");
    $monitor ("time %g   x %d   outNP %b   outPN %b clr %b %d",$time, x, outP,  outN, clr,i);
    $dumpvars(0,  ZC);
    #200 x=13'd0; clr=0;
    #200 x=13'd0; clr=1;
    #200 x=13'd0; clr=1;
    #200 x=13'd0; clr=1;
    #200 x=13'd0; clr=0;
    #200 x=13'd0; clr=0;
    #200 x=13'd0; clr=0;
    #200 x=13'd0; clr=0;
    #200 x=0;
    #200 x=0;
    #200 x=0;
    #200 x= 0;
    /*
    #200 x= 1000; $display("%d   %d ",x, out, delay);
    for (i=0; i<100; i=i+1)
        #200 x= x/1.01; 
    for (i=0; i<100; i=i+1)
        #200 x= 0; 
    #200 x= 0;
    for (i=0; i<5; i=i+1)
        #200 x= 1 ; 

    for (i=0; i<10; i=i+1)
        #200 x= -1; 
    for (i=0; i<5; i=i+1)
        #200 x=1; 

    for (i=0; i<10; i=i+1)
        #200 x=-1; 
    for (i=0; i<10; i=i+1)
        #200 x= 1; 
*/
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= -1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 1; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 0; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 0; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 0; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 0; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 0; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);
     #200 x= 0; $display("time %g  %d PN %b NP %b",$time, x, outP,  outN);


    $finish;
  end
  always begin
       clk = 1'b0;
       forever #100 clk = ~clk; // Toggle clock every 5 ticks
  end

endmodule
