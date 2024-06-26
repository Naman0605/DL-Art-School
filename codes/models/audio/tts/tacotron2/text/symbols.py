from models.audio.tts.tacotron2.text import cmudict

_pad = '_'
_punctuation = '|!\'(),.:;? '
_special = '-'
_letters = 'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षज्ञत्रश्रऽािीुूृॄॅॆेैॉॊोौ्ॐ॓॔ॠ'  

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet

