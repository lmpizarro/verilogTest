`include "one_shot.v"
`timescale 1ns/1ps

module one_shot_tb();

integer i;
reg clk, in, reset, load;
reg [7:0] data_dur;
wire out;
// in: pulse
// out: level
//

periodic_pulse DUT (clk, in, out, data_dur, load, reset);

  initial 
    begin
    // vcd dump
    $dumpfile("simple.vcd");
    // the variable 's' is what GTKWave will label the graphs with
    $dumpvars(0, DUT);

      $monitor ( "time: %2g   clk: %b in: %b out: %b data_dur: %b load: %b" , $time, clk, in, out, data_dur, load);
      reset = 1'b0;
      load = 1'b0;
      data_dur = 8'b00001111;
      in = 1'b0;
      clk = 1'b1;
      #10 reset = 0;
      #10 reset = 1;
      #10 reset = 1;
      #10 reset = 1; 
      #10 reset = 0;
      #10 reset = 0;
      #10 reset = 0;
      #10 reset = 0; load = 1'b1;
      #10 reset = 0;
      #10 reset = 0;
      #10 reset = 0; in = 1'b1;
      #10 reset = 0; in = 1'b1;
      #10 reset = 0; in = 1'b1;
      #10 reset = 0; in = 1'b0;
      #10 reset = 0;
      #10 reset = 0;
      for (i = 0; i < 2500; i = i + 1)
        #10 reset = 0;

      $finish;
    end

   always begin
     #10 clk = ~clk; // Toggle clock every 5 ticks
   end
endmodule
