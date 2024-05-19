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
            }
        }
    }
}'''

