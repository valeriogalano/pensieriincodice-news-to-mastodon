<div align="center">
  <img src="https://raw.githubusercontent.com/valeriogalano/pensieriincodice-assets/main/images/pensieriincodice-logo-telegram-community.png" alt="Logo Progetto" width="150"/>
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
    <a href="https://www.satispay.com/en-it/qrcode/?qrcode=https%3A%2F%2Fwww.satispay.com%2Fdownload%2Fqrcode%2FS6Y-CON--EC548199-5F32-4BD6-AAF5-73A999744E56" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/dona con-Satispay-E62E1A?style=for-the-badge&logo=satispay&logoColor=white" alt="Dona con Satispay"></a>
    <a href="https://www.paypal.com/donate/?hosted_button_id=HRKMD7X43R7SS" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/dona con-Paypal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="Dona con Paypal"></a>
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
    <a href="https://pensieriincodice.it/">Podcast</a> | 
    <a href="https://www.linkedin.com/in/valeriogalano/">LinkedIn</a>
  </p>
</div>
