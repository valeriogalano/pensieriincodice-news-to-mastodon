<div align="center">
  <img src="https://cdn.pensieriincodice.it/images/pensieriincodice-locandina.png" alt="Logo Progetto" width="150"/>
  <h1>Pensieri In Codice - News to Mastodon</h1>
  <p>
    Il progetto ha lo scopo di pubblicare le news di PIC sull'account Mastodon del podcast.
  </p><p>    
    Le news vengono prelevate da Readwise.
  </p>
  
  <p>
    <img src="https://img.shields.io/github/stars/valeriogalano/pensieriincodice-news-to-mastodon?style=for-the-badge" alt="GitHub Stars"/>
    <img src="https://img.shields.io/github/forks/valeriogalano/pensieriincodice-news-to-mastodon?style=for-the-badge" alt="GitHub Forks"/>
    <img src="https://img.shields.io/github/last-commit/valeriogalano/pensieriincodice-news-to-mastodon?style=for-the-badge" alt="Last Commit"/>
    <a href="https://pensieriincodice.it/sostieni" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/sostieni-Pensieri_in_codice-fb6400?style=for-the-badge" alt="Sostieni Pensieri in codice"></a>
  </p>
</div>

---

## Installazione in locale

Per installare il progetto in locale, è necessario avere Python 3.11 installato.

### Variabili di ambiente

Imposta nel tuo IDE o sul suo sistema operativo le seguenti variabili di ambiente:

```
MASTODON_TOKEN="<MASTODON_TOKEN_HERE>"
TELEGRAM_MESSAGE_TEMPLATE="<TELEGRAM_MESSAGE_TEMPLATE>"
READWISE_ACCESS_TOKEN="<READWISE_ACCESS_TOKEN>"
```

- `MASTODON_TOKEN`: token di Mastodon
- `MASTODON_MESSAGE_TEMPLATE`: template del messaggio
- `READWISE_ACCESS_TOKEN`: token di accesso di Readwise

La variabile `MASTODON_MESSAGE_TEMPLATE` deve contenere i seguenti placeholder:

- `{title}`: il titolo dell'articolo
- `{notes}`: le note dell'articolo
- `{link}`: il link dell'articolo

Esempio:
"{title}\n{notes}\n\n{link}"

### Installazione dei requisiti

```bash
pip install -r requirements.txt
```

Puoi eseguire `main.py` per verificare il funzionamento dello script.

```bash
python main.py
```

---

## Contributi

Se noti qualche problema o hai suggerimenti per migliorare l'organizzazione, sentiti libero di aprire una **Issue**
e successivamente una **Pull Request**. Ogni contributo è ben accetto!

---

## Importante

Vorremmo mantenere questo repository aperto e gratuito per tutti,
ma lo scraping del contenuto di questo repository NON È CONSENTITO.
Se ritieni che questo lavoro ti sia utile e vuoi utilizzare qualche risorsa,
ti preghiamo di citare come fonte il podcast e/o questo repository.

---

<div align="center">
  <p>
    Realizzato con ❤️ da <strong>Valerio Galano</strong>
  </p>
  <p>
    <a href="https://valeriogalano.it/">Sito Web</a> | 
    <a href="https://daredevel.com/">Blog</a> | 
    <a href="https://pensieriincodice.it/">Podcast</a>
  </p>
</div>
