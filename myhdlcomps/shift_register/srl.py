'''
8-bit Shift-Left Register with 
Positive-Edge Clock,
Serial In, and 
Serial Out

IO Pins Description
-------------------
C Positive-Edge Clock
SI Serial In
SO Serial Output
'''

# Verilog Code

'''
Following is the Verilog code for an 8-bit shift-left register with a
positive-edge clock, serial in, and serial out.

module shift (C, SI, SO);
 input C,SI;
 output SO;
 reg [7:0] tmp;

 always @(posedge C)
  begin
   tmp = tmp << 1;
   tmp[0] = SI;
  end
 assign SO = tmp[7];
endmodule
'''
import myhdl
from myhdl import *

@block
def srl(clk, si, so):
    q = intbv(0)[8:] 
	
    @always(clk.posedge)
    def seq():
         so.next = q[7]
         q[8:1] = q[7:]
         q[0] = si

    return seq

@block
def srlpiso(clk, pi, load, so):
    q = intbv(0)[8:]
	
    @always(clk.posedge)
    def seq():  
      if load:
         q.next = pi
      else:
         so.next = q[7]
         q[8:1] = q[7:]

    return seq
 
@block
def ram(dout, din, addr, we, clk, Nbits=8, depth=128):
    """  Ram model """
    
    mem = [Signal(intbv(0)[Nbits:]) for i in range(depth)]
    
    @always(clk.posedge)
    def write():
        if we:
            mem[addr].next = din
                
    @always_comb
    def read():
        dout.next = mem[addr]
    return write, read

@block
def delay_1(dout, din, clk, Nbits = 8):
 
    mem = Signal(intbv(0)[Nbits:])
   
    
    @always(clk.posedge)
    def write():
            dout.next = mem
            mem.next = din
    return write

@block
def diff_disp(dout, din, clk, disp, Nbits = 8):
 
    mem = Signal(intbv(0)[Nbits:])
   
    
    @always(clk.posedge)
    def write():
            dout.next = din - (mem >> disp)
            mem.next = din
    return write

@block
def logical_slr(din, disp, dout):
    
    @always(din or disp)
    def proc():
        if disp == 0:
            dout.next = din
        elif disp == 1:
            dout.next = din << 1
        elif disp == 2:
            dout.next = din << 2
        elif disp == 3:
            dout.next = din << 3
 
    return proc

@block
def logical_slr_b(din, disp, dout):
    
    @always(din or disp)
    def proc():
            dout.next = din << disp
 
    return proc

@block
def comparator(A,B,gt, eq, lt):

  @always_comb
  def proc():
   if A > B:
      gt.next  = 1
      eq.next = 0
      lt.next = 0
   elif A < B:
      gt.next  = 0
      eq.next = 0
      lt.next = 1
   else:
      gt.next  = 0
      eq.next = 1
      lt.next = 0

  return proc


@block
def attenuator(sig, att, sig_out):

    @always(sig)
    def atte():
        if att == 0:
            sig_out.next = sig
        elif att == 1:
            sig_out.next = (sig>>1) + (sig>>2)
        elif att == 2:
            sig_out.next = sig>>1
        elif att == 3:
            sig_out.next = ((sig>>1) + (sig>>2))>>2
        elif att == 4:
            sig_out.next = sig>>2
        elif att == 5:
            sig_out.next = ((sig>>2) + (sig>>3))>>2
        elif att == 6:
            sig_out.next = sig>>3
        elif att == 7:
            sig_out.next = ((sig>>4) + (sig>>3))>>2
        elif att == 8:
            sig_out.next = sig>>4
        elif att == 9:
            sig_out.next = ((sig>>4) + (sig>>5))>>2
        elif att == 10:
            sig_out.next = sig>>5
        elif att == 11:
            sig_out.next = ((sig>>6) + (sig>>5))>>2
        elif att == 12:
            sig_out.next = sig>>6
        elif att == 13:
            sig_out.next = ((sig>>6) + (sig>>7))>>2
        elif att == 14:
            sig_out.next = sig>>7
        elif att == 15:
            sig_out.next = ((sig>>8) + (sig>>7))>>2
    return atte


@block
def multiplier_4bits(clk, B, A, out, Nbits=4):
    '''
      out = B * A

            B
           *A
           --
           out
    '''

    mem = [Signal(intbv(0)[2*Nbits:]) for i in range(Nbits)]


    @always(clk.posedge)
    def mult_():
        C = (mem[0] + mem[1]) + (mem[2] + mem[3])

    @always_comb
    def calcs():
       mem[0][5:].next = A[0]&B
       mem[1][6:].next =  A[1]&B
       mem[2][7:].next =  A[3]&B
       mem[3][8:].next =  A[4]&B

       mem[0][8:4].next = 0
       mem[1][8:5].next = 0
       mem[1][0].next = 0
       mem[2][8:6].next = 0
       mem[2][2:0].next = 0
       mem[3][3:0].next = 0

    return mult_, calcs 

@block
def partial_mult( B, A, mem0, mem1, mem2, mem3):

   @always(A,B)
   def calcs():
    while(1):
       mem0[5:].next = A[0]&B
       mem1[6:].next =  A[1]&B
       mem2[7:].next =  A[3]&B
       mem3[8:].next =  A[4]&B

       mem0[8:4].next = 0
       mem1[8:5].next = 0
       mem1[0].next = 0
       mem2[8:6].next = 0
       mem2[2:0].next = 0
       mem3[3:0].next = 0

   return calcs 

@block
def full_adder(Cin, A,B, S, Cout):

   @always(A,B)
   def calcs():
        axorb = A^B
        S.next = axorb^Cin
        Cout.next = A&B | axorb&Cin

   return calcs 

@block
def adder(Cin, A,B, S, Cout):

   @always(A,B)
   def calcs():
      C1 = 0
      full_adder(Cin, A[0], B[0], S[0], C1)
      full_adder(C1, A[1], B[1], S[1], Cout)
   return calcs 


@block
def dff(q, d, clk):
   @always(clk.posedge)
   def logic():
     q.next = d

   return logic


@block
def register_(q, d, clk):
   ff0 = dff(q[0], d[0], clk)
   ff1 = dff(q[1], d[1], clk)
   ff2 = dff(q[2], d[2], clk)
   ff3 = dff(q[3], d[3], clk)
   ff4 = dff(q[4], d[4], clk)
   ff5 = dff(q[5], d[5], clk)
   ff6 = dff(q[6], d[6], clk)
   ff7 = dff(q[7], d[7], clk)

   @always(clk.posedge)
   def seq():
       q[0].next = d[0]
       q[1].next = d[1]
       q[2].next = d[2]
       q[3].next = d[3]
       q[4].next = d[4]
       q[5].next = d[5]
       q[6].next = d[6]
       q[7].next = d[7]
   return seq

@block
def register(q, d, clk, Nbits):
   ffs=[dff(q[i], d[i], clk) for i in range(Nbits)]
   @always(clk.posedge)
   def seq():
     for i in range (Nbits):
         q[i].next = d[i]
   return seq


@block
def addSat (A, B, C, Nbits=16):
  maxNeg = -2**(Nbits-1)
  maxPos = 2**(Nbits-1) - 1


  tmp =Signal(intbv(0)[Nbits+1:])

  @always(A,B)
  def comb():
   tmp.next = A + B

   if tmp<maxNeg: 
       tmp.next=maxNeg
   if tmp>maxPos:
       tmp.next=maxPos
   C.next = tmp[Nbits:0]

  return comb

