#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Tools to work with Finnish in Python
# Cody Daniels, Copyright 2017

from __future__ import unicode_literals

vowels = ['a','A','o','O','u','U','e','E','i','I','ä','Ä','ö','Ö','y','Y']

def vowel_harmony(word):
	"""Determines whether a string uses front or back vowels."""
	if any(vowel in word for vowel in ['a','o','u']):
		return 'back'
	return 'front'

def syllables(word):
	"""Identifies the syllables in a string (for consonant gradation). Returns a hyphenated string."""
	characters = list(word)
	vowels_and_consonants = list()
	for char in characters:
		if char in vowels:
			vowels_and_consonants.append('V')
		else:
			vowels_and_consonants.append('C')
	indices = []
	diphthongs = ['ai','ei','oi','ui','yi','äi','öi','au','eu','iu','ou','ey','iy','äy','öy','ie','uo','yö']
	for index, char in enumerate(vowels_and_consonants):
		if char == 'V':
			if vowels_and_consonants[index - 1] == 'C' and index - 1 >= 0:
				if vowels_and_consonants[index - 2] == 'C' and index - 2 >= 0:
					if vowels_and_consonants[index - 3] == 'C' and index - 3 >= 0:
						if vowels_and_consonants[index - 4] == 'V' and index - 4 >= 0:
							# VCC-CV
							indices.append(index - 1)
					elif vowels_and_consonants[index - 3] == 'V' and index - 3 >= 0:
						# VC-CV
						indices.append(index - 1)
				elif vowels_and_consonants[index - 2] == 'V' and index - 2 >= 0:
					# V-CV
					indices.append(index - 1)
			elif vowels_and_consonants[index - 1] == 'V' and index - 1 >= 0:
				if not characters[index - 1] + characters[index] in diphthongs:
					if characters[index - 1] != characters[index]:
						# V-V (not a diphthong or long vowel)
						indices.append(index)
	for i, index in enumerate(indices):
		word = word[0:index + i] + '-' + word[index + i:]
	return word

def strong_to_weak(word):
	"""Consonant gradation."""
	consonant_pairs = {'kk':'k ','pp':'p ','tt':'t ','k':'','p':'v','t':'d','lt':'ll','nk':'ng','nt':'nn','mp':'mm','rt':'rr','lki':'lje','lke':'lje','rki':'rje','rke':'rje','hke':'hje','uku':'uvu','yky':'yvy','bb':'b','gg':'g','hje':'hkke','lje':'lkke','oia':'oja','sk':'skk','tk':'tkk','hk':'hkk','sp':'spp','st':'stt'}
	characters = list(word)
	for index, char in enumerate(characters):
		if index < len(characters) - 2 and char + characters[index + 1] + characters[index + 2] in consonant_pairs:
			# triple strong charaters found
			replacement = list(consonant_pairs[char + characters[index + 1] + characters[index + 2]])
			characters[index] = replacement[0]
			characters[index + 1] = replacement[1]
			characters[index + 2] = replacement[2]
			if len(replacement) == 4:
				characters.insert(index + 3, replacement[3])
		elif index < len(characters) - 1 and char + characters[index + 1] in consonant_pairs:
			# double strong charaters found
			replacement = list(consonant_pairs[char + characters[index + 1]])
			characters[index] = replacement[0]
			characters[index + 1] = replacement[1]
			if len(replacement) == 3:
				characters.insert(index + 2, replacement[2])
		elif char in consonant_pairs and index != 0:
			# single strong charater found
			characters[index] = consonant_pairs[char]
	for char in characters:
		if char == ' ':
			characters.remove(' ')
	return word + ''.join(characters)

def weak_to_strong(word):
	"""Reverse consonant gradation."""
	consonant_pairs = {'k':'kk','rr':'rt','v':'p','mm':'mp','p':'pp','t':'tt','d':'t'}
	characters = list(word)
	for index, char in enumerate(characters):
		if index < len(characters) - 2 and char + characters[index + 1] + characters[index + 2] in consonant_pairs:
			# triple weak charaters found
			replacement = list(consonant_pairs[char + characters[index + 1] + characters[index + 2]])
			characters[index] = replacement[0]
			characters[index + 1] = replacement[1]
			characters[index + 2] = replacement[2]
			if len(replacement) == 4:
				characters.insert(index + 3, replacement[3])
		elif index < len(characters) - 1 and char + characters[index + 1] in consonant_pairs:
			# double weak charaters found
			replacement = list(consonant_pairs[char + characters[index + 1]])
			characters[index] = replacement[0]
			characters[index + 1] = replacement[1]
			if len(replacement) == 3:
				characters.insert(index + 2, replacement[2])
		elif char in consonant_pairs and index != 0:
			# single weak charater found
			characters[index] = consonant_pairs[char]
	for char in characters:
		if char == ' ':
			characters.remove(' ')
	return ''.join(characters)

def genitive(stem):
	"""Returns the genitive form of a word."""
	if stem[:1].isupper() and not any(vowel in stem[-1:] for vowel in vowels):
		# is a proper noun that ends in a consonant
		genitive = strong_to_weak(stem) + 'in'
	elif stem[-3:] == 'nen':
		genitive = strong_to_weak(stem[:-3]) + 'sen'
	else:
		# ends in a vowel or is not a proper noun and ends in a consonant
		genitive = strong_to_weak(stem) + 'n'
	return genitive

def accusative(stem):
	"""Returns the accusative form of a word."""
	if stem[:1].isupper() and not any(vowel in stem[-1:] for vowel in vowels):
		# is a proper noun that ends in a consonant
		accusative = strong_to_weak(stem) + 'in'
	elif stem[-3:] == 'nen':
		accusative = strong_to_weak(stem[:-3]) + 'sen'
	else:
		# ends in a vowel or is not a proper noun and ends in a consonant
		accusative = strong_to_weak(stem) + 'n'
	return accusative

def partitive(stem):
	"""Returns the partitive form of a word."""
	harmony = vowel_harmony(stem)
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
	else:
		# ends in consonant
		if harmony == 'front':
			partitive = stem + 'tä'
		else:
			partitive = stem + 'ta'
	return partitive

def inessive(stem):
	"""Returns the inessive form of a word."""
	harmony = vowel_harmony(stem)
	if harmony == 'front':
		inessive = strong_to_weak(stem) + 'ssä'
	else:
		inessive = strong_to_weak(stem) + 'ssa'
	return inessive

def elative(stem):
	"""Returns the elative form of a word."""
	harmony = vowel_harmony(stem)
	if harmony == 'front':
		elative = strong_to_weak(stem) + 'stä'
	else:
		elative = strong_to_weak(stem) + 'sta'
	return elative

def illative(stem):
	"""Returns the illative form of a word."""
	if any(vowel in stem[-1:] for vowel in vowels):
		if any(vowel in stem[-2:][:1] for vowel in vowels):
			# ends in two vowels
			if len(list(stem)) < 4:
				# less than 4 letters
				illative = stem + 'h' + stem[-1:] + 'n'
			else:
				# 4 letters or more
				if stem[-2:][:1] == stem[-1:]:
					# last two vowels are the same
					illative = stem + 'seen'
				else:
					# last two vowels are different
					illative = stem + stem[-1:] + 'seen'
		else:
			# ends in one vowel
			illative = stem + stem[-1:] + 'n'
	else:
		illative = stem + 'iin'
	return illative

def adessive(stem):
	"""Returns the adessive form of a word."""
	harmony = vowel_harmony(stem)
	if harmony == 'front':
		adessive = strong_to_weak(stem) + 'llä'
	else:
		adessive = strong_to_weak(stem) + 'lla'
	return adessive

def ablative(stem):
	"""Returns the ablative form of a word."""
	harmony = vowel_harmony(stem)
	if harmony == 'front':
		ablative = strong_to_weak(stem) + 'ltä'
	else:
		ablative = strong_to_weak(stem) + 'lta'
	return ablative

def allative(stem):
	"""Returns the allative form of a word."""
	allative = strong_to_weak(stem) + 'lle'
	return allative

def essive(stem):
	"""Returns the essive form of a word."""
	harmony = vowel_harmony(stem)
	if harmony == 'front':
		essive = stem + 'nä'
	else:
		essive = stem + 'na'
	return essive

def translative(stem):
	"""Returns the translative form of a word."""
	translative = strong_to_weak(stem) + 'ksi'
	return translative

def instructive(stem):
	"""Returns the instructive form of a word."""
	instructive = strong_to_weak(stem) + 'in'
	return instructive

def abessive(stem):
	"""Returns the abessive form of a word."""
	harmony = vowel_harmony(stem)
	if harmony == 'front':
		abessive = strong_to_weak(stem) + 'ttä'
	else:
		abessive = strong_to_weak(stem) + 'tta'
	return abessive

def comitative(stem):
	"""Returns the comitative form of a word."""
	comitative = stem + 'ne-'
	return comitative

def decline(stem):
	"""Declines a word. Returns a dictionary."""
	return {
		'nominative': stem,
		'genitive': genitive(stem),
		'accusative': accusative(stem),
		'partitive': partitive(stem),
		'inessive': inessive(stem),
		'elative': elative(stem),
		'illative': illative(stem),
		'adessive': adessive(stem),
		'ablative': ablative(stem),
		'allative': allative(stem),
		'essive': essive(stem),
		'translative': translative(stem),
		'instructive': instructive(stem),
		'abessive': abessive(stem),
		'comitative': comitative(stem)
	}

def verb_type(verb):
	"""Determines the type of a verb for conjugation."""
	if any(vowel in verb[-1:] for vowel in vowels):
		if any(vowel in verb[-2:][:1] for vowel in vowels):
			# ends in two vowels
			if verb[-1:] == 'a' or verb[-1:] == 'ä':
				verb_type = 1
			else:
				verb_type = 3
		elif verb[-2:] == 'da' or verb[-2:] == 'dä':
			verb_type = 2
		elif verb[-2:] == 'ta' or verb[-2:] == 'tä':
			if verb[-3:][:1] == 'e':
				verb_type = 6
			elif verb[-3:][:1] == 'i':
				verb_type = 5
			else:
				verb_type = 4
		else:
			verb_type = 3
	else:
		verb_type = 3
	return verb_type
	
def conjugate(verb):
	"""Conjugates a verb in the present tense. Returns a dictionary."""
	conjugation = verb_type(verb)
	harmony = vowel_harmony(verb)
	if harmony == 'front':
		he_end = 'vät'
	else:
		he_end = 'vat'
	if conjugation == 1:
		return {
			'minä': strong_to_weak(verb[:-1]) + 'n',
			'sinä': strong_to_weak(verb[:-1]) + 't',
			'hän': verb[:-1] + verb[-2:][:1],
			'me': strong_to_weak(verb[:-1]) + 'mme',
			'te': strong_to_weak(verb[:-1]) + 'tte',
			'he': verb[:-1] + he_end
		}
	elif conjugation == 2:
		return {
			'minä': verb[:-2] + 'n',
			'sinä': verb[:-2] + 't',
			'hän': verb[:-2],
			'me': verb[:-2] + 'mme',
			'te': verb[:-2] + 'tte',
			'he': verb[:-2] + he_end
		}
	elif conjugation == 3:
		return {
			'minä': weak_to_strong(verb[:-2]) + 'en',
			'sinä': weak_to_strong(verb[:-2]) + 'et',
			'hän': weak_to_strong(verb[:-2]) + 'ee',
			'me': weak_to_strong(verb[:-2]) + 'emme',
			'te': weak_to_strong(verb[:-2]) + 'ette',
			'he': weak_to_strong(verb[:-2]) + 'e' + he_end
		}
	elif conjugation == 4:
		han_form = verb[:-2] + verb[-2:][1:]
		last_three = list(verb[-3:])
		if last_three[0] == last_three[1] == last_three[2]:
			last_three[2] = ''
		han_form.join(last_three)
		return {
			'minä': weak_to_strong(verb[:-2] + verb[-2:][1:]) + 'n',
			'sinä': weak_to_strong(verb[:-2] + verb[-2:][1:]) + 't',
			'hän': weak_to_strong(han_form),
			'me': weak_to_strong(verb[:-2] + verb[-2:][1:]) + 'mme',
			'te': weak_to_strong(verb[:-2] + verb[-2:][1:]) + 'tte',
			'he': weak_to_strong(verb[:-2] + verb[-2:][1:]) + he_end
		}
	elif conjugation == 5:
		return {
			'minä': verb[:-2] + 'tsen',
			'sinä': verb[:-2] + 'tset',
			'hän': verb[:-2] + 'tsee',
			'me': verb[:-2] + 'tsemme',
			'te': verb[:-2] + 'tsette',
			'he': verb[:-2] + 'tse' + he_end
		}
	else:
		return {
			'minä': verb[:-2] + 'nen',
			'sinä': verb[:-2] + 'net',
			'hän': verb[:-2] + 'nee',
			'me': verb[:-2] + 'nemme',
			'te': verb[:-2] + 'nette',
			'he': verb[:-2] + 'ne' + he_end
		}