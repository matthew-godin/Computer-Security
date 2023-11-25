import numpy as np
#from matplotlib import pyplot as plt
ciphertext = 'agpygmqgxyxfiuimypmvcmssvuiyjcggxripiuxyjrlkwdivxkwtyqxtexhmquxejdjtswxfikrdiprgxdlcgqpyvmjcrsqypumcfwrqqoelwcqkxritspgfepgomrhgtorbwqrwelcesxwghgvkxgspwlyrmpxrikelsbmrcqjmeqiuxorbwvszvmxggdxficrsqyphvyqbepkovzctixhcvkrqmrpgwcgmrutsgsswwziplctcmrqccliqekhdlyxkjmsjstmxkgwoesrjcrvyxcgvmfirlgvosskjxdszidydjcadvskfxncmsjstinelmoevwrlgvoepijsgititryxyjgameqiumxafmelfmtmfgypmvuebirlgqcijzgwzvmxggdmtivloogrijswfitmdwcphxrsskjwyfpmildpwgqpyvchkwlclsoikrqicwixmwgidlcfnyolyvosxmxiuasxfxjigeritexhrlgfsvbeumdhyvvwkpmrixriqxtikqjsqocejqqwdpgogeppywjspwsrnmqlrhgwovrepmwejwcvokcrgvkpjcvlogmpqvyjrlghowcvvxryqjqvsrqxcrmirlgpsslxjikrrinsziyrfxriumnhnslogckvcenpcelhesvspifmxhcifwkcqgcryrrvkwdvyqkrdlchgwovrajibilikxripxtiowzvwwramsfryvczgrerbynedmmrqjdlcwwvpeaicjpsphvlowjmildiqxrvyxcgvmyrrskxcjmiuewsbmhmmermqryjasnsbeqwkqspyxghdsrlcxyjrlgwevpswrnmlkeserrvamcezwqpexcparogcwuebcfipgoagxjsexcbeizxgspxristribtjyoeqimjgzovwfkvnelhcpcsrlgjevmjcpvxfiuqkpjitqkqkenwkrbxjicogrqjkpjxjicryogwkrbpkdkvbwkwyjmrgyxmdstqcelhesvspxjixivxrssrrmuxriasnsbsdxjiwerytimerittspjetwcskiqjglggjebizvqaxxfmutbszedpiqyogwdlcgcxovnmnpkvczgrwspiesxwnmeyyyqeosxkrlgkbicrnikzcwvlkruswpnsrlgvgmqididlcgcwopcxwwcicxjixafivlovrlglkfgxuspxfikrciaxymvprltsgelcnmqlryrsxxfitmnhjiylkxuswpncmyfssjwswaovcedmqgyxgvzmjpcvglwpkooqmwvsdlcvfipilwgpowqgtikxsvgwissaqyvhdighlclmildelhnmogmreikpchdcnewwqhyxfiuimerittspjetwglcrvloqmvpmxkjmildgmqgwdlccevoinhqaxxfiuxoqmjvlojmsftvelxcrnpgiesxgceninekspkdlcxjmmofitfkkcephnvwwvmmoqephviyzgwxiyvvlokpswrnelhkxswmfxmyyqxjedylhgvcyalembgsquxkraiuxrizvqaxgmpqvbiypncliasoicenvqxogrmqrsxkmildmlhginfcetkeibxjedxfieediptkpvepwjefmlkdimskidvyalgqrmiypghdlcquivzcwqrdlcktserbephdlyxyigipitifipwkrqxfiuxkxcshxrmlkufexrlkwswlsvwyfcgcyciulkpoacqccceweueqilitevvspgxrerpcvqiaevibtgpnebwdighlclmildelhnmogmreikpchdcnewmvmcfwrqqoelwcpgewwvlogywgxrerxjiiepidvyalwqqosdxjiwwrmnpbirekrsrexjiqvcipgypmvyiwewxjixgmrepehcxjedxfijelmrshgyraicpsrexjiwwcpxicfwhccmekihmbwrephdlyxvlofpsyrmsjstmcejevibeberxkxgsp'

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

key_length = 6


# frequency analysis on the entire ciphertext
def frequency_analysis(ciphertext: ''):
    '''calculates the number of occurence of each character'''
    
    # count the number of occurances in the ciphertext given
    return np.char.count(ciphertext, letters)

    ################### plotting ###################     
    # x = np.array(letters)
    # y = np.array(result)
    # plt.title('Frequency Analysis on Whole ciphertext')
    # plt.xlabel('letters')
    # plt.ylabel('number of occurance')
    # plt.bar(x, y, align = 'center')
    # plt.show()

def finding_chunks(ciphertext: '', key_length: int):
    '''separates the ciphertext with given key length'''

    minimal_chunk_size = len(ciphertext) // key_length
    excluded_maximal_chunk_size_max_index = len(ciphertext) % key_length
    chunk_array = []
    # initialize empty array of chunks
    for i in range(key_length):
        chunk_array.append([' '] * (minimal_chunk_size + (1 if i < excluded_maximal_chunk_size_max_index else 0)))

    # loop through the ciphertext and obtain elements with indexes as follows:
    # (0,6,12,18...) (1,7,13,19...) (2,8...) until (5,11,...)
    for i in range(len(ciphertext)):
        chunk_array[i % key_length][i // key_length] = ciphertext[i]
    
    result = []
    for i in range(key_length):
        result.append(''.join(chunk_array[i]))
        
    return result

def find_most_occuring_letter_index(frequency: []):
    '''given a chunks frequency, find the most occuring letter's index on the alphabet'''
    temp = np.array(frequency)
    return np.argmax(frequency)


def secret_key(ciphertext: '', key_length: int):
    '''given a ciphertext and its key length, find the key'''
    key_array = [' '] * key_length
    
    chunks = finding_chunks(ciphertext, key_length)
    
    chunks_frequency = []
    # frequency analysis on each of the chunks
    for i in range(key_length):
        chunks_frequency.append(frequency_analysis(chunks[i]))

        # for each chunk, need to find the most occuring letter's index
        most_commom_char = find_most_occuring_letter_index(chunks_frequency[i])
        
        # As 'e' is the most common letter in English sentences, the
        # most common letter should be 'e' and its shift should be
        # a shift from 'e'
        e_index = ord('e') - ord('a')
        if most_commom_char > e_index:
            key_array[i] = chr(len(letters) - most_commom_char + ord('e'))
        elif most_commom_char < e_index:
            key_array[i] = chr(ord('e') - most_commom_char)
        else:
            key_array[i] = chr(most_commom_char)
    
    # Q2 prints
    print('Chunked text ------------------------------------')
    print(chunks)

    # Q3 prints
    print('KEY ---------------------------------------------')
    key = ''.join(key_array)
    print(key)
    return key

def decrypt(ciphertext: '', key: []):
    '''decrpyt the ciphertext using key'''
    plaintext_array = [' '] * len(ciphertext)
    for i in range(len(ciphertext)):
        plaintext_array[i] = chr((ord(ciphertext[i]) - ord('a') + ord(key[i % len(key)]) - ord('a'))
            % len(letters) + ord('a'))

    plaintext = ''.join(plaintext_array)
    print('Plaintext -----------------------------------------')
    print(plaintext)
    return plaintext

# Q1
print('Frequency Analysis on whole cipher --------------------------')
print(frequency_analysis(ciphertext))

# Q2, 3, 4
key = secret_key(ciphertext, key_length)
decrypt(ciphertext, key)