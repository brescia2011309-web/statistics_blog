import unicodedata
from collections import Counter

text = '''Lunedí 13 settembre. Les Salines
È uno scenario piuttosto straordinario quest’
abbozzo di città abbandonata
ai bordi di un villaggio e al margine dei secoli. Ho percorso una metà
dell’
emiciclo, ho salito la gradinata del padiglione centrale, e per un pezzo
sono rimasta a contemplare questi edifici costruiti per fini utilitari e che non
sono mai serviti a niente. Sono solidi, esistono, eppure il fatto di essere
abbandonati li trasforma in un simulacro fantastico; di che cosa, non si sa.
L’
erba calda, sotto il cielo d’
autunno, e l’
odore delle foglie morte
’
m
assicuravano che non avevo lasciato questo mondo, ma ero tornata
indietro, nel passato, di duecento anni. Sono andata a prendere della roba
nella macchina; ho steso in terra una coperta, vi ho posato dei cuscini, la radio
a transistor, e mi sono messa a fumare, ascoltando Mozart. Dietro due o tre
finestre polverose indovinavo delle presenze: sono sicuramente uffici. Un
camion si è fermato davanti a uno dei pesanti portoni, alcuni uomini l'hanno
aperto, hanno caricato dei sacchi nel cassone. Nient’
altro ha turbato il silenzio
di questo pomeriggio: nessun visitatore. Finito il concerto, mi son messa a
leggere. Mi sentivo doppiamente spaesata: me ne andavo lontano, lungo la
riva di un fiume sconosciuto: alzavo gli occhi, e mi ritrovavo in mezzo a
queste pietre, lontana dalla mia vita.
Poiché la cosa piú sorprendente è la mia presenza qui, e il fatto che mi
senta cosí allegra. Temevo la solitudine di questo ritorno verso Parigi. Finora,
quando non c
’è Maurice, le bambine mi accompagnavano in tutti i miei
viaggi. Pensavo che avrei sentito la mancanza dei rapimenti di Colette, delle
esigenze di Lucienne. E invece, ecco che provo un tipo di gioia che avevo del
tutto dimenticato. Un senso di libertà che mi ringiovanisce di vent’
anni. Al punto che, chiuso il libro, mi sono messa a scrivere, per me stessa, come a
vent’
anni.
Ogni volta che mi separo da Maurice, non è mai a cuor leggero. Il
congresso dura appena una settimana, eppure, mentre andavamo da Mougins
all’
aeroporto di Nizza, avevo la gola stretta. Anche lui era commosso. Quando
l’
altoparlante ha chiamato i viaggiatori per Roma, mi ha abbracciata forte,
–
Sta
’
attenta a non ammazzarti, in macchina.
– Sta
’
attento a non ammazzarti
in aereo –
. Prima di scomparire si è voltato ancora una volta: c
’
’
era un
ansia,
nei suoi occhi, che mi ha toccata a fondo. Il decollo mi è parso drammatico. I
quadrimotori partono pian piano, è un lungo arrivederci. Il jet si è strappato
da terra con la brutalità di un addio.
Ma ben presto ho cominciato a sentirmi felice. No, l’
assenza delle mie figlie
non mi rattristava, al contrario. Potevo guidare in fretta, o piano, come mi
pareva, andare dove volevo, fermarmi dove mi saltava. Ho deciso di passare
questa settimana a vagabondare. Mi alzo con la luce del giorno. La macchina
mi aspetta sulla strada, in cortile, come un animale fedele: è umida di rugiada;
le asciugo gli occhi, e fendo gioiosamente la giornata che comincia a indorarsi
di sole. Posata accanto a me, la mia sacca bianca con le carte Michelin, la
Guide bleu, dei libri, un golf, le sigarette, è una compagna di viaggio piena di
discrezione. Nessuno si secca quando chiedo alla padrona dell’
albergo la
ricetta del suo pollo ai gamberi.
Sta per scendere la sera, ma l’
aria è ancora tiepida. È uno di quei momenti
toccanti, in cui la terra è cosí ben intonata agli uomini che sembra impossibile
che tutti non siano felici.
Martedí 14 settembre
Una delle cose che piacevano tanto a Maurice è l’intensità di quella che lui
chiamava «la mia attenzione alla vita». Durante questo breve colloquio a tu
per tu con me stessa, si è rianimata. Ora che Colette è sposata, e Lucienne è in
America, avrò tutte le possibilità di coltivarla.
– Ti annoierai. Dovresti
metterti a fare qualcosa, prenderti un lavoro,
– mi ha detto Maurice a
Mougins. Ha insistito. Ma, almeno per ora, non ne sento il bisogno.
Finalmente, voglio vivere un po’
per me stessa. E approfittare con Maurice di
questa solitudine a due di cui siamo stati privati per tanto tempo. Ho un
mucchio di progetti in testa.'''

# Normalize accents to base characters
normalized = unicodedata.normalize('NFKD', text)
base = ''.join(ch for ch in normalized if not unicodedata.combining(ch))

# Keep only ASCII letters a-z
clean = ''.join(ch.lower() for ch in base if ch.isalpha())
# Now filter to a-z only (removes non-latin letters if any)
clean = ''.join(ch for ch in clean if 'a' <= ch <= 'z')

counter = Counter(clean)

# Sort by letter
letters = sorted(counter.items())
max_count = max(counter.values()) if counter else 0

print('Letter counts:')
for letter, count in letters:
    print(f"{letter}: {count}")

print('\nHTML snippet (bars):')
for letter, count in letters:
    width = int(count / max_count * 100)
    print(f"<div class=\"bar-row\"><div class=\"bar-label\">{letter}</div><div class=\"bar-fill\" style=\"width:{width}%\">{count}</div></div>")
