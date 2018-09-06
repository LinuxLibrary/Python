#!/usr/bin/env python3

"""Model for aircraft flights"""

class Flight:
	"""A flight with a particular passenger aircraft."""
	
	def __init__(self, number, aircraft):
		if not number[:2].isalpha():
			raise ValueError("No airline code in '{}'".format(number))
		
		if not number[:2].isupper():
			raise ValueError("Invalid airline code '{}'".format(number))
			
		if not (number[2:].isdigit() and int(number[2:]) <= 9999):
			raise ValueError("Invalid route number '{}'".format(number))
			
		self._number = number
		self._aircraft = aircraft
		
		rows, seats = self._aircraft.seating_plan()
		self._seating = [None] + [ {letter:None for letter in seats} for _ in rows ]
		
	def number(self):
		return self._number
		
	def airline(self):
		return self._number[:2]
		
	def aircraft_model(self):
		return self._aircraft.model()

	def allocate_seat(self, passenger):
		"""Allocate a seat to a passanger.
	
		Args:
			seat: A seat designator such as '12C' or '21F'.
			passenger: The passenger name.

		Raises:
			ValueError: If the seat i unavailable.
		"""
		rows, seat_letters = self._aircraft.seating_plan()
		
		letter = seat[-1]
		if letter not in seat_letters:
			raise ValueError("Invalid seat letter {}".format(letter))

		row_text = seat[:-1]
		try:
			row = int(row_text)
		except ValueError:
			raise ValueError("Invalid seat row {}".format(row_text))
		
		if row not in rows:
			raise ValueError("Invalid row number {}".format(row))
	
		if self._seating[row][letter] is not None:
			raise ValueError("Seat {} already occupied".format(seat))
		
		self._seating[row][letter] = passenger

	def aircraft_registration(self):
		return self._aircraft.registration()
		
	def aircraft_seating_plan(self):
		return self._aircraft.seating_plan()	

		
class Aircraft:

	def __init__(self, registration, model, num_rows, num_seats_per_row):
		self._registration = registration
		self._model = model
		self._num_rows = num_rows
		self._num_seats_per_row = num_seats_per_row
		
	def registration(self):
		return self._registration
		
	def model(self):
		return self._model
		
	def seating_plan(self):
		return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])
		

'''
Sample execution:
from 01-AirTravel import *

a = Aircraft("G-EUPT", "Airbus A139", num_rows=22, num_seats_per_row=6)
a.registration()
a.model()
a.seating_plan()

f = Flight("BA758", Aircraft("G-EUPT", "Airbus A139", num_rows=22, num_seats_per_row=6))
'''
