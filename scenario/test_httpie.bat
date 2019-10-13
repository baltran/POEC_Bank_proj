http --auth Sadia:Sadia POST http://localhost:5000/api/tokens
http GET http://localhost:5000/api/comptes/2/operations "Authorization:Bearer "
http PUT http://localhost:5000/api/comptes/2/depot valeur=50 "Authorization:Bearer "
http PUT http://localhost:5000/api/comptes/2/retrait valeur=60.5 motif="achat de noël" "Authorization:Bearer "
http PUT http://localhost:5000/api/comptes/2/virement valeur=20 compte_dest=1 "Authorization:Bearer "
