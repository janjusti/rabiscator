# Rabiscator

Apply a PNG image to a PDF file.

1. Clone this repo
2. Create a folder called `input`
3. Set your target PDF and PNG files on `input`
4. Create a `.env` file:
```bash
BASENAME="RandomDoc"
SOMENUMBER="1234"
SOMENAME="John Doe"
IMG_POS="200,100,600,300"
```
5. Run:
```bash
docker compose up
```