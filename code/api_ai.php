<?php
# Main Script: api_ai.php
# PHP script
require_once ".config.php";
function bot_request( $module, $params ) {
  $ch = curl_init();
  curl_setopt( $ch, CURLOPT_URL, "{$GLOBALS[ "BOT_API_HOST" ]}/api/v1/ai/{$module}/" );
  curl_setopt( $ch, CURLOPT_CUSTOMREQUEST, "POST" );
  curl_setopt( $ch, CURLOPT_POST, 1 );
  curl_setopt( $ch, CURLOPT_POSTFIELDS, json_encode( $params ) );
  curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1 );
  curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1 );

  /** IMPORTANTE: Estas opciones deshabilitan la verificación SSL. ( NO RECOMENDADO )  */
  curl_setopt( $ch, CURLOPT_SSL_VERIFYHOST, false );
  curl_setopt( $ch, CURLOPT_SSL_VERIFYPEER, false );
  /** */

  $headers = array();
  $headers[] = "Content-Type: application/json";
  $headers[] = "Auth: {$GLOBALS[ "BOT_API_ID" ]}";
  $headers[] = "Authorization: {$GLOBALS[ "BOT_API_TOKEN" ]}";

  curl_setopt( $ch, CURLOPT_HTTPHEADER, $headers );
  $response = json_decode( curl_exec( $ch ), TRUE );

  if( curl_errno( $ch ) ) {
    $MESSAGE = curl_error( $ch );
    $CODE = curl_errno( $ch );
    throw new \Exception( $MESSAGE, $CODE );
  } else if( $response[ "status" ] !== 200 ) {
    throw new \Exception( $response[ "message" ], $response[ "status" ] );
  }
  curl_close( $ch );
  return $response;
}

/** COMPOSER MODULE */
/**************/

/** designer: method */
$params = array( 
  "method" => "designer", 
  "args" => array( 
    "prompt" => "Imagen 3d de un perro westie vestido como vikingo", // Description of the required image
    "n" => 1, // Number of images to generate (Max: 5)
    "size" => "512x512" // Image size ( 1024x1024 | 512x512 | 256x256 )
  ) 
);
$response = bot_request( "composer", $params );
echo "JSON Response: " . json_encode( $response );

/** writer: method */
$params = array(
  "method" => "writer", 
  "args" => array( 
    "instruction" => "Redacta una mensaje de felicitación de cumpleaños para los clientes de mi cafetería" // Indication to generate the text
  ) 
);
$response = bot_request( "composer", $params );
echo "JSON Response: " . json_encode( $response );

/** rewriter: method */
$params = array( 
  "method" => "rewriter", 
  "args" => array( 
    "input" => "Al parecer la implementación del api, no es complicada en lo absoluto", // Text to edit
    "instruction" => "traduce el texto al ingles" // Editing statement
  ) 
);
$response = bot_request( "composer", $params );
echo "JSON Response: " . json_encode( $response );

/**********************************************************************************************************************/


/** TRAINING MODULE */
/**********************************************************************************************************************/
/** learn: method */
$params = array(
  "method" => "learn", 
  "args" => array( 
    "tag" => "SALUDO_001", // Unique identification tag. ( IMPORTANT: This data allows the modification of the learning text )
    "input" => base64_encode( "Hola, bienvenido a The Coffee Coop, en que puedo ayudarte?" ), // Natural language text
    "keywords" => "", // Words to be interpreted by the AI engine to generate the responses
    "actions" => array() // Callback actions
  ) 
);
$response = bot_request( "training", $params );
echo "JSON Response: " . json_encode( $response );

/** learning_file: method */
$params = array(
  "method" => "learning_file", 
  "args" => "https://xxxxxxxxx.xxx/resources/es_trainig_data.xlsx" // URL of the file to upload
);
$response = bot_request( "training", $params );
echo "JSON Response: " . json_encode( $response );

/** relearning: method */
$params = array( 
  "method" => "relearning" 
  // Does not require additional arguments
);
$response = bot_request( "training", $params );
echo "JSON Response: " . json_encode( $response );

/** learnings_get: method */
$params = array( 
  "method" => "learnings_get",
  "args" => array( 
    "format" => "xlsx" // File Format: .xlsx | .json
  )
);
$response = bot_request( "training", $params );
echo "JSON Response: " . json_encode( $response );

/**********************************************************************************************************************/


/** BOT MODULE */
/**********************************************************************************************************************/

/** reply: method */
$params = array(
  "method" => "reply",
  "args" => array( 
    "input" => "Hola buenos días", // requisitos de usuario
    "max" => 2 // Número máximo de respuestas solicitadas (IMPORTANTE: En un chatbot es recomendable solicitar la respuesta más coincidente)
    // Solo como prueba, solicitamos las 2 respuestas más coincidentes
  )
);
$response = bot_request( "bot", $params );
echo "JSON Response: " . json_encode( $response );

/** reply: method */
$params = array(
  "method" => "reply",
  "args" => array( 
    "input" => "Donde estan ubicados?",
    "max" => 1
  )
);
$response = bot_request( "bot", $params );
echo "JSON Response: " . json_encode( $response );

/** reply: method */
$params = array(
  "method" => "reply",
  "args" => array( 
    "input" => "Al parecer no puedes ayudarme que puedo hacer?",
    "max" => 1
  )
);
$response = bot_request( "bot", $params );
echo "JSON Response: " . json_encode( $response );

/**********************************************************************************************************************/

?>