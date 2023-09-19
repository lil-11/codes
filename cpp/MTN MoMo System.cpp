#include <iostream>
#include <string>

using namespace std;

int main () {
	int balance = 500;
	int pin = 20050;
	
	cout << "Welcome to MTN MoMo"<<endl;
	cout << "1. Send Money"<<endl;
	cout << "2. Pay Bills/Services"<<endl;
	cout << "3. Buy Airtime/Bundles"<<endl;
	cout << "4. MomoPay"<<endl;
	cout << "5. Bank Operations"<<endl;
	cout << "6. Loans"<<endl;
	cout << "7. My Account"<<endl;
	cout << "8. Help"<<endl;
	cout << "9. Promo"<<endl;
	
	int choice;
	cin >> choice;
	
	switch (choice) {
		case 1:
			cout << "Send Money"<<endl;
			cout << "11. To MTN Number"<<endl;
			cout << "12. To other Networks"<<endl;
			cout << "13. To client with no account"<<endl;
			cout << "14. For withdrawal"<<endl;
			cout << "15. Cash-out security"<<endl;
			
			int choicee;
			cin >> choicee;
			
			switch (choicee) {
				case 11:
					int number;
					int amount;
					int Ref;
					int pinn;
					cout << "Enter phone number: ";
					cin >> number;
					cout << "Enter amount: ";
					cin >> amount;
					
					if (amount <= balance) {
						cout << "Enter Ref (Reason for transfer): ";
						cin >> Ref;
						
						cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
						cin >> pinn;
						
						if (pin == pinn) {
							balance -= amount;
							cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
						}
						else {
							cout << "Your MM PIN is invalid"<<endl;
							return 0;
						}
					} 
					else {
						cout << "Insufficient funds. Kindly recharge your MoMo account."<<endl;
						return 0;
					}
					break;
					
				case 12:
					cout << "To other networks"<<endl;
					cout << "121. Cameroon"<<endl;
					cout << "122. Gabon"<<endl;
					cout << "123. Congo Braz"<<endl;
					cout << "124. RCA"<<endl;
					cout << "125. Chad"<<endl;
					cout << "126. Equatorial Guinea"<<endl;
					
					int choices;
					
					cin >> choices;
					
					switch (choices) {
						case 121:
							cout << "Cameroon"<<endl;
							cout << "1211. Orange Money"<<endl;
							cout << "1212. CBC Wallet"<<endl;
							cout << "1213. Express Union"<<endl;
							cout << "1214. BICEC Wallet"<<endl;
							cout << "1215. CCA Wallet"<<endl;
							cout << "1216. UBC"<<endl;
							cout << "1217. La Regionale"<<endl;
							cout << "1218. Sara"<<endl;
							cout << "1219. M2U CMR"<<endl;
							cout << "12110. YOOME Money"<<endl;
							cout << "12120. BGFI Mobile"<<endl;
							
							int cchoice;
							
							cin >> cchoice;
							
							switch (cchoice) {
								case 1211:
									int number;
									int amount;
									int Ref;
									int pinn;
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Insufficient funds. Kindly recharge your MoMo account."<<endl;
										return 0;
									}
									
									break;
									
								case 1212:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									
									break;
									
								case 1213:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Insufficient funds. Kindly recharge your MoMo account."<<endl;
										return 0;
									}
									
									break;
									
								case 1214:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1215:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1216:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1217:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1218:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1219:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}
									break;
									
								case 12110:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 12120:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								default: 
								cout << "Invalid option, arborting"<<endl;
								return 0;
							}
							
							break;
							
						case 122:
							cout << "Gabon"<<endl;
							cout << "1221. Airtel Gabon"<<endl;
							cout << "1222. BGFI Gabon"<<endl;
							cout << "1223. MOOV Gabon"<<endl;
							
							int chhoice;
							cin >> chhoice;
							
							switch (chhoice) {
								case 1221:
									int number;
									int amount;
									int Ref;
									int pinn;
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}
									break;
									
								case 1222:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1223:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}
									break;
									
								
								default:
									cout << "Invalid option, aborting"<<endl;
									return 0;
							}
							
					
							break;
							
						case 123:
							cout << "Congo Braz"<<endl;
							cout << "1231. MTN Congo"<<endl;
							cout << "1232. Airtel Congo"<<endl;
							cout << "1233. BCI Mobile"<<endl;
							cout << "1234. BGFIBANK Congo"<<endl;
							
							int chooice;
							cin>> chooice;
							
							switch (chooice) {
								case 1231:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}
									break;
								
								case 1232:
								cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}	
									break;
									
								case 1233:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								case 1234:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
								
								default: 
								cout << "Invalid option aborting"<<endl;
								return 0;
							}
							break;
							
						case 124:
							cout << "RCA"<<endl;
							cout << "1241. Orange Centrafrique"<<endl;
							cout << "1242. BSIC Centrafrique"<<endl; 
							
							int choiice;
							cin >> choiice;
							
							switch (choiice) {
								case 1241:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}	
									break;
									
								case 1242:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
									
								default:
									cout << "Invalid option, aborting"<<endl;
									return 0;
							}
							break;
							
						case 125:
							cout << "Chad"<<endl;
							cout << "1251. Airtel Chad"<<endl;
							cout << "1252. Moov Chad"<<endl;
							cout << "1253. BSCI_Chad"<<endl;
							
							int choicce;
							cin>>choicce;
							
							switch (choicce) {
								case 1251:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}	
									break;
									
								case 1252:
									cout << "Enter phone number: ";
									cin >> number;
									cout << "Enter amount: ";
									cin >> amount;
									
									if (amount <= balance) {
										cout << "Enter Ref (Reason for transfer): ";
										cin >> Ref;
										
										cout << "Enter PIN to confirm the transfer of "<<amount<< "FCFA to " <<number<<". Reference: "<<Ref<<endl;
										cin >> pinn;
										
										if (pin == pinn) {
											balance -= amount;
											cout << "Succesful transfer of "<<amount<<" FCFA to "<<number<<". Balance: FCFA "<<balance<<endl;
										}
										else {
											cout << "Your MM PIN is invalid"<<endl;
											return 0;
										}
									} 
									else {
										cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again"<<endl;
										return 0;
									}	
									break;
									
								case 1253:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
								default:
									cout << "Invalid option, aborting!!";
									return 0;
							}
							break;
							
						case 126:
							cout << "Equatorial Guinea"<<endl;
							cout << "1261. BGFI Mobile"<<endl;
							
							int choicee;
							cin >> choicee;
							
							switch (choicee) {
								case 1261:
									cout << "Sorry, kindly go to 'Bank Operations' (5) for this transaction" <<endl;
									return 0;
									break;
								default:
									cout << "Invalid option, Aborting!!!"<<endl;
									return 0;
							}
							
							break;
						
						default: 
						cout << "Invalid option, aborting!!"<<endl;
						return 0;
					}
					
					break;
					
				
				case 13:
				    cout << "To client with no account" << endl;
				    cout << "131. Cameroon" << endl;
				    cout << "132. Congo Braz" << endl;
				    cout << "133. Gabon" << endl;
				    cout << "134. Chad" << endl;
				
				    int choice;
				    cin >> choice;
				
				    switch (choice) {
				        case 131:
				            cout << "Enter phone number: ";
				            cin >> number;
				            cout << "Enter amount: ";
				            cin >> amount;
				
				            if (amount <= balance) {
				                cout << "Enter Ref (Reason for transfer): ";
				                cin >> Ref;
				
				                cout << "Enter PIN to confirm the transfer of " << amount << " FCFA to " << number << ". Reference: " << Ref << endl;
				                cin >> pin;
				
				                if (pin == pinn) {
				                    balance -= amount;
				                    cout << "Successful transfer of " << amount << " Kindly send transfer number ********* to the receiver. New balance: FCFA " << balance << endl;
				                }
				                else {
				                    cout << "Your MM PIN is invalid" << endl;
				                }
				            }
				            else {
				                cout << "Sorry, you do not have enough money to perform this transaction. Please refill your account from the nearest Mobile Money point and try again" << endl;
				            }
				            break;
				
				        case 132:
				            cout << "Tppcongobrazz" << endl;
				            break;
				
				        case 133:
				            string name;
				            cout << "Veuillez entrer le numero du destinataire precede du code pays (exple: 241xxxxxxxx pour le Gabon): ";
				            cin >> number;
				
				            cout << "Ecrire le nom du beneficiare tel que sur the piece d identite: ";
				            cin >> name;
				
				            cout << "Le beneficiaire retirera la montant recu dans les agencies Express Union. Veuillez entrer le montant du transfer (FCFA): ";
				            cin >> amount;
				
				            if (amount < 500 || amount > 500000) {
				                cout << "Le montant saisi est incorrect. Le montant doit etre compris entre 500 et 500 000 FCFA." << endl;
				                cout << "Veuillez reessayer SVP." << endl;
				            }
				            else {
				                balance -= amount;
				                cout << "Transfert reussi de " << amount << " FCFA to " << name << ". Nouvelle balance " << balance << " FCFA" << endl;
				            }
				            break;
				
				        case 134:
				        	
				            cout << "Weel" << endl;
				              break;
				
				        default:
				            cout << "Invalid option, Aborting!!!" << endl;
				            break;
				    }
				    
				    break;
						
				case 14:
					
					break;
					
				case 15:
					
					break;
					
				case 16:
					
					break;
				
				default:
					cout << "Invalid option, aborting!!"<<endl;
					return 0;
			}
		
		break;
		
		case 2:
			
			break;
			
		case 3:
			
			break;
			
		case 4:
			
			break;
			
		case 5:
			
			break;
			
		case 6:
			
			break;
			
		case 7:
			
			break;
			
		case 8:
			
			break;
			
		case 9:
			
			break;
		
		default:
			cout << "Invalid option, aborting!!"<<endl;
			return 0;
	}
	return 0;
}
