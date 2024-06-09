import json 
My_App_Strings = '''
{
    "MainWindows": {
        "Name": {
            "fr": "OfficeAssistant",
            "en": "OfficeAssistant",
            "es": "AsistenteDeOficina",
            "ge": "BüroAssistent"
        }
    },
    "Common": {
        "FilesTypeSelection": {
            "fr": "Images compatibles",
            "en": "Compatible pictures",
            "es": "Imágenes compatibles",
            "ge": "Kompatible bilder"
        }
    },
    "File_Extension": {
        "Obfuscation": {
            "fr": "Obfusqué",
            "en": "Obfuscated",
            "es": "Ofuscado",
            "ge": "Verschleiert"
        },
    "Watermark": {
            "fr": "Filigrané",
            "en": "Watermarked",
            "es": "Marca",
            "ge": "Wasserzeichen"
        }
    },
    "Buttons": {
        "AddFiles": {
            "fr": "Ajouter",
            "en": "Add",
            "es": "Añadir",
            "ge": "Hinzufügen"
        },
        "Reset": {
            "fr": "Suppr.",
            "en": "Reset",
            "es": "Reset",
            "ge": "Reset"
        },
        "Convert": {
            "fr": "Convertir",
            "en": "Convert",
            "es": "Convertir",
            "ge": "Konvertieren"
        },
        "Exit": {
            "fr": "Quitter",
            "en": "Exit",
            "es": "Salir",
            "ge": "Beenden"
        },
        "Validate": {
            "fr": "Valider",
            "en": "Validate",
            "es": "Validar",
            "ge": "Bestätigen"
        },
        "OpenFile": {
            "fr": "Ouvrir",
            "en": "Select",
            "es": "Abrir",
            "ge": "Öffnen"
        },
        "Test": {
            "fr": "Test",
            "en": "Test",
            "es": "Prueba",
            "ge": "Test"
        },
        "TextModification": {
            "fr": "Editer",
            "en": "Edit",
            "es": "Editar",
            "ge": "ändern"
        }
    },
    "Tab1": {
        "TabName": {
            "fr": "Créateur de Pdf",
            "en": "Pdf Creator",
            "es": "Creador de Pdf",
            "ge": "Pdf-Ersteller"
        },
        "PannelHeader": {
            "Column1": {
                "fr": "Position",
                "en": "Position",
                "es": "Posición",
                "ge": "Position"
            },
            "Column2": {
                "fr": "Nom du fichier",
                "en": "File name",
                "es": "Nombre del archivo",
                "ge": "Dateiname"
            },
            "Column3": {
                "fr": "Chemin",
                "en": "Path",
                "es": "Ruta",
                "ge": "Pfad"
            }
        },
        "SaveFile": {
            "WindowName": {
                "fr": "Nommez votre fichier",
                "en": "Name your file",
                "es": "Nombre su archivo",
                "ge": "Benenne deine Datei"
            },
            "Instruction": {
                "fr": "Nom du fichier :",
                "en": "File Name :",
                "es": "Nombre del archivo :",
                "ge": "Dateiname :"
            }
        },
        "SelectFiles": {
            "fr": "Sélectionner plusieurs fichiers",
            "en": "Select many files",
            "es": "Seleccionar varios archivos",
            "ge": "Mehrere Dateien auswählen"
        }
    },
    "Tab2": {
        "TabName": {
            "fr": "Offuscation d'image",
            "en": "Picture offuscation",
            "es": "Ofuscación de imagen",
            "ge": "Bildobfuskation"
        },
        "Instruction": {
            "fr": "Selectionnez une image",
            "en": "Select a picture",
            "es": "Seleccionar una imagen",
            "ge": "Wählen Sie ein Bild"
        }
    },
    "Processing": {
        "PictureSaving": {
            "fr": "Image convertie : {} / {}",
            "en": "Picture conversion: {} / {}",
            "es": "Conversión de imagen: {} / {}",
            "ge": "Bildumwandlung: {} / {}"
        },
        "PdfSaving": {
            "fr": "Enregistrement du PDF",
            "en": "Saving pdf",
            "es": "Guardando pdf",
            "ge": "PDF speichern"
        },
        "FileSaving": {
            "fr": "Enregistrement du fichier",
            "en": "Saving file",
            "es": "Guardando archivo",
            "ge": "Datei speichern"
        },
        "UpdateProcessing": {
            "fr": "...",
            "en": "...",
            "es": "...",
            "ge": "..."
        },
        "FinishPdfSaving": {
            "fr": "PDF enregistré",
            "en": "Pdf saved..",
            "es": "PDF guardado..",
            "ge": "PDF gespeichert.."
        },
        "FinishFileSaving": {
            "fr": "Fichier enregistré !",
            "en": "File saved !",
            "es": "Archivo guardado !",
            "ge": "Datei gespeichert !"
        },
        "AreasProcessing": {
            "fr": " zone(s) d'obfuscation traitée(s) sur ",
            "en": " obfuscation zones treated out of ",
            "es": " zonas de ofuscación tratadas de ",
            "ge": " Obfuskationszonen behandelt von "
        },
        "AreasNumber": {
            "fr": " zones créé(s)",
            "en": " created",
            "es": " zonas creadas",
            "ge": "erstellt"
        }
    },
    "Tab3": {
        "TabName": {
            "fr": "Ajouter un filigrane",
            "en": "Add a watermark",
            "es": "Filigrana",
            "ge": "Wasserzeichen"
        },
        "Init_Watermark_Text": {
            "fr": "Filigrané le ",
            "en": "Watermarked on ",
            "es": "Filigrana el",
            "ge": "Wasserzeichen am"
        },
        "Edit_Watermark_Text": {
            "WindowName": {
                "fr": "Éditez le filigrane",
                "en": "Edit watermark",
                "es": "Editar la marca de agua",
                "ge": "Bearbeiten Sie das Wasserzeichen"
            },
            "Instruction": {
                "fr": "Éditez le filigrane",
                "en": "Edit watermark",
                "es": "Editar la marca de agua",
                "ge": "Bearbeiten Sie das Wasserzeichen"
            },
            "WaterMark_Color": {
                "fr": "Couleur",
                "en": "Color",
                "es": "Color",
                "ge": "Farbe"
            },
            "WaterMark_Transparency": {
                "fr": "Transparence",
                "en": "Transparency",
                "es": "Transparencia",
                "ge": "Transparenz"
            },
            "WaterMark_FontSize": {
                "fr": "Taille du texte",
                "en": "Font Size",
                "es": "Tamano del texto",
                "ge": "Textgröße"
            },
            "WaterMark_Space_Between_Text": {
                "fr": "Inter lignes",
                "en": "Inter lines",
                "es": "líneas internas",
                "ge": "Inter-Linien"
            },
            "WaterMark_Text": {
                "fr": "Texte",
                "en": "Text",
                "es": "Texto",
                "ge": "Text"
            }
        },
        "Edit_Watermark_Buttons":{
            "Cancel":{
                "fr": "Annuler",
                "en": "Cancel",
                "es": "Anular",
                "ge": "Stornieren"
        },
            "Preview":{
                "fr": "Aperçu",
                "en": "Preview",
                "es": "Avance",
                "ge": "Vorschau"
        },
            "Close":{
                "fr": "Fermer",
                "en": "Close",
                "es": "Cerca",
                "ge": "Schließen"
        }
        
        }
        
    
    },
    "MessageBox": {
        "Type": {
            "Error": {
                "fr": "Erreur",
                "en": "Error",
                "es": "Error",
                "ge": "Fehler"
            },
            "Info": {
                "fr": "Info",
                "en": "Info",
                "es": "Información",
                "ge": "Info"
            },
            "Confirmation": {
                "fr": "Confirmation",
                "en": "Confirmation",
                "es": "Confirmación",
                "ge": "Bestätigung"
            }
        },
        "Message": {
            "NoTitle": {
                "fr": "Donnez un titre au document qui va être créé",
                "en": "Define a name for the document you are creating",
                "es": "Defina un nombre para el documento que está creando",
                "ge": "Geben Sie einen Namen für das zu erstellende Dokument an"
            },
            "BadSavePath": {
                "fr": "Chemin de sauvegarde manquant",
                "en": "File saving path is missing",
                "es": "Falta la ruta de guardado del archivo",
                "ge": "Speicherpfad der Datei fehlt"
            },
            "NoPicture": {
                "fr": "Pas d'image selectionnée",
                "en": "No picture selected",
                "es": "No se ha seleccionado ninguna imagen",
                "ge": "Kein Bild ausgewählt"
            },
            "Error_Cancelation": {
                "fr": "Vous avez annulé",
                "en": "Canceled",
                "es": "Cancelado",
                "ge": "Abgebrochen"
            },
            "Info_ProcessFinished": {
                "part1": {
                    "fr": "Fichier pdf créé avec succès Détails:",
                    "en": "Pdf file successfully created Details:",
                    "es": "Archivo pdf creado con éxito Detalles:",
                    "ge": "PDF-Datei erfolgreich erstellt Details:"
                },
                "part1.1": {
                    "fr": "- Nombre d'images : ",
                    "en": "- Number of pictures: ",
                    "es": "- Número de imágenes: ",
                    "ge": "- Anzahl der Bilder: "
                },
                "part2": {
                    "fr": "- Nom du fichier : ",
                    "en": "- File name: ",
                    "es": "- Nombre del archivo: ",
                    "ge": "- Dateiname: "
                },
                "part3": {
                    "fr": "- Chemin : ",
                    "en": "- Path: ",
                    "es": "- Ruta: ",
                    "ge": "- Pfad: "
                }
            },
            "Info_Reset": {
                "fr": "Voulez-vous faire un reset des images selectionnées",
                "en": "Do you want to reset all selected pictures?",
                "es": "¿Quiere restablecer todas las imágenes seleccionadas?",
                "ge": "Möchten Sie alle ausgewählten Bilder zurücksetzen?"
            },
            "Info_Reset_Tab2": {
                "fr": "Voulez vous en plus supprimer l'image selectionnée",
                "en": "Moreover do you want to delete the selected picture?",
                "es": "Además, ¿desea eliminar la imagen seleccionada?",
                "ge": "Möchten Sie außerdem das ausgewählte Bild löschen?"
            },
            "Info_FileSaved": {
                "fr": "Fichier sauvegardé",
                "en": "File saved",
                "es": "Archivo guardado",
                "ge": "Datei gespeichert"
            },
            "ChangeLanguage": {
                "fr": "Si vous changez de langue, vous perdrez vos modifications. Voulez vous continuer ?",
                "en": "If you change languages, you will lose your changes. Do you want to continue?",
                "es": "Si cambia de idioma, perderá los cambios. ¿Quieres continuar?",
                "ge": "Wenn Sie die Sprache ändern, gehen Ihre Änderungen verloren. Möchtest du fortfahren?"
            },
            "EmptyField": {
                "fr": "Le champs est resté vide, ajoutez au moins 1 caractère",
                "en": "The field remained empty, add at least 1 character.",
                "es": "El campo quedó vacío, añade al menos 1 carácter.",
                "ge": "Das Feld ist leer geblieben, fügen Sie mindestens 1 Zeichen hinzu."
            },
            "LoadingTimeHighDefinition": {
                "fr": "Image en haute definition, le chargement est en cours, veuillez patientez quelques secondes",
                "en": "High-definition picture, loading in progress, please wait a few seconds.",
                "es": "Imagen de alta definición, carga en progreso, por favor espere unos segundos.",
                "ge": "Hochauflösendes Bild, Laden läuft, bitte warten Sie einige Sekunden."
            },
            "LoadingTimeNormalDefinition": {
                "fr": "Le chargement est en cours, veuillez patientez quelques secondes",
                "en": "Loading in progress, please wait a few seconds.",
                "es": "Carga en progreso, por favor espere unos segundos.",
                "ge": "Laden läuft, bitte warten Sie einige Sekunden."
            },
            "LoadingTime": {
                "fr": "Le chargement est en cours, veuillez patientez quelques secondes",
                "en": "Loading in progress, please wait a few seconds.",
                "es": "Carga en progreso, por favor espere unos segundos.",
                "ge": "Laden läuft, bitte warten Sie einige Sekunden."
            }
        }
    }
}'''

