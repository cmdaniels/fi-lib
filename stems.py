# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from fi_lib import vowel_harmony

stems = [
	'tukka',
	'kakku',
	'pappi',
	'tippa',
	'katto',
	'juttu',
	'tikka',
	'huppu',
	'rotta',
	'harakka',
	'anoppi',
	'ammatti',
	'lika',
	'maku',
	'rako',
	'tuke',
	'halko',
	'jalka',
	'virka',
	'nahka',
	'niska',
	'matka',
	'lanka',
	'linko',
	'puku',
	'suku',
	'tiuku', # WIP
	'raaka', # WIP
	'piispa',
	'kalpa',
	'varpu',
	'ripa',
	'sopu',
	'tapa',
	'kampa',
	'rumpu',
	'sota',
	'pata',
	'kita',
	'rinta',
	'kanto',
	'ranta',
	'ilta',
	'kulta',
	'parta',
	'kerta',
	'vahti',
	'kosto',
	'hyvä',
	'hampurilainen',
	'maa',
	'tietokone',
	'Pasi',
	'Sanna',
	'Fang',
	'Janet'
]

vowels = ['a','o','u','e','i','ä','ö','y']

for stem in stems:
	harmony = vowel_harmony(stem)
	# GRAMMATICAL CASES
	# Genitive Case (Singular)
	# used to express ownership and possession, as an attribute, with postpositions, and with the verb 'täytyy'
	genitive = '¯\_(ツ)_/¯'
	if stem[:1].isupper() and not any(vowel in stem[-1:] for vowel in vowels):
		# is a proper noun that ends in a consonant
		genitive = stem + 'in'
	elif stem[-3:] == 'nen':
		genitive = stem[:-3] + 'sen'
	else:
		# ends in a vowel or is not a proper noun and ends in a consonant
		genitive = stem + 'n'
	# Partitive Case (Singular)
	# used with greetings, wishes, indefinite quantities ('some'), numbers greater than 1, and some verbs
	partitive = '¯\_(ツ)_/¯'
	if stem[-1:] == 'e':
		# ends in 'e'
		if harmony == 'front':
			partitive = stem + 'ttä'
		else:
			partitive = stem + 'tta'
	elif stem[-3:] == 'nen':
		# ends in 'nen'
		if harmony == 'front':
			partitive = stem[:-3] + 'stä'
		else:
			partitive = stem[:-3] + 'sta'
	elif any(vowel in stem[-1:] for vowel in vowels):
		if any(vowel in stem[-2:][:1] for vowel in vowels):
			# ends in two vowels
			if harmony == 'front':
				partitive = stem + 'tä'
			else:
				partitive = stem + 'ta'
		else:
			# ends in one vowel
			if harmony == 'front':
				partitive = stem + 'ä'
			else:
				partitive = stem + 'a'
	elif not any(vowel in stem[-1:] for vowel in vowels):
		# ends in consonant
		if harmony == 'front':
			partitive = stem + 'tä'
		else:
			partitive = stem + 'ta'
	# INTERNAL LOCATIVE CASES
	# Inessive Case (Singular)
	# in
	inessive = '¯\_(ツ)_/¯'
	if harmony == 'front':
		inessive = stem + 'ssä'
	else:
		inessive = stem + 'ssa'
	# Elative Case (Singular)
	# from (inside)
	elative = '¯\_(ツ)_/¯'
	if harmony == 'front':
		elative = stem + 'stä'
	else:
		elative = stem + 'sta'
	# Illative Case (Singular)
	# (in)to
	illative = '¯\_(ツ)_/¯'
	# EXTERNAL LOCATIVE CASES
	# Adessive Case (Singular)
	# at, on
	adessive = '¯\_(ツ)_/¯'
	if harmony == 'front':
		adessive = stem + 'llä'
	else:
		adessive = stem + 'lla'
	# Ablative Case (Singular)
	# from (outside)
	ablative = '¯\_(ツ)_/¯'
	if harmony == 'front':
		ablative = stem + 'ltä'
	else:
		ablative = stem + 'lta'
	# Allative Case (Singular)
	# (on)to
	allative = '¯\_(ツ)_/¯'
	allative = stem + 'lle'
	# MARGINAL CASES
	# Essive Case (Singular)
	# as
	essive = '¯\_(ツ)_/¯'
	if harmony == 'front':
		essive = stem + 'nä'
	else:
		essive = stem + 'na'
	# Translative Case (Singular)
	# into (change, transformation, NOT movement)
	translative = '¯\_(ツ)_/¯'
	traslative = stem + 'ksi'
	# Instructive Case (Singular)
	# with, using
	instructive = '¯\_(ツ)_/¯'
	# Abessive Case (Singular)
	# without
	abessive = '¯\_(ツ)_/¯'
	if harmony == 'front':
		abessive = stem + 'ttä'
	else:
		abessive = stem + 'tta'