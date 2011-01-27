#! /usr/bin/perl

#    Extract statistics from a PCSC profiling file
#    Copyright (C) 2007,2011  Ludovic Rousseau <ludovic.rousseau@free.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# example input file:

# Start a new profile
#SCardEstablishContext 204
#SCardIsValidContext 0
#SCardIsValidContext 0
#SCardListReaderGroups 1
#SCardFreeMemory 1
#SCardListReaders 31
#SCardListReaders 60
#SCardGetStatusChange 27
#SCardConnect 15696
#SCardTransmit 2917
#SCardControl 1931
#SCardGetSetAttrib 127
#SCardFreeMemory 2
#SCardGetSetAttrib 110
#SCardFreeMemory 1
#SCardGetSetAttrib 82
#SCardGetSetAttrib 175
#SCardGetSetAttrib 84
#SCardStatus 99
#SCardFreeMemory 1
#SCardFreeMemory 35
#SCardReconnect 112033
#SCardDisconnect 90851
#SCardFreeMemory 2
#SCardReleaseContext 171

# Result:
#(6)	SCardFreeMemory: 42 µs
#(5)	SCardGetSetAttrib: 578 µs
#(2)	SCardIsValidContext: 0 µs
#(2)	SCardListReaders: 91 µs
#(1)	SCardDisconnect: 90851 µs
#(1)	SCardTransmit: 2917 µs
#(1)	SCardGetStatusChange: 27 µs
#(1)	SCardStatus: 99 µs
#(1)	SCardReconnect: 112033 µs
#(1)	SCardConnect: 15696 µs
#(1)	SCardEstablishContext: 204 µs
#(1)	SCardControl: 1931 µs
#(1)	SCardListReaderGroups: 1 µs
#(1)	SCardReleaseContext: 171 µs
#total: 224641 µs
#
#Percentages:
#49.87%: SCardReconnect
#40.44%: SCardDisconnect
#6.99%: SCardConnect
#1.30%: SCardTransmit
#0.86%: SCardControl
#0.26%: SCardGetSetAttrib
#0.09%: SCardEstablishContext
#0.08%: SCardReleaseContext
#0.04%: SCardStatus
#0.04%: SCardListReaders
#0.02%: SCardFreeMemory
#0.01%: SCardGetStatusChange
#0.00%: SCardIsValidContext
#0.00%: SCardListReaderGroups


use strict;
use warnings;

my (@l, %r, %n, $k, $t);

while (<>)
{
	next if not m/^SCard/;

	@l = split ' ';
	#print $l[1];
	$r{$l[0]} += $l[1];
	$n{$l[0]}++;
}

$t = 0;
undef @l;
foreach $k (keys %r)
{
	push @l, sprintf "(%d)\t%s: %d µs\n", $n{$k}, $k, $r{$k};
	$t += $r{$k};
}

print reverse sort {my $c = $a; my $d = $b; $c =~ s/.*\((.*)\).*/$1/; $d
=~ s/.*\((.*)\).*/$1/; $c <=> $d} @l;
print "total: $t µs\n";

undef @l;
print "\nPercentages:\n";
foreach $k (keys %r)
{
	push @l, sprintf "%2.2f%%: %s\n", $r{$k}/$t*100, $k;
}
print reverse sort {my $c = $a; my $d = $b; $c =~ s/(.*)%.*/$1/; $d =~ s/(.*)%.*/$1/; $c <=> $d} @l;
